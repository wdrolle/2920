"""
    Inherent Risk 
    
    Generates Risk Assessments for each code in the JSON file using a language model,
    and saves the output as a JSON file.
    
"""
import os
import json
import re
import requests

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_to_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def clean_and_chunk_text(text):
    cleaned_text = re.sub(r'\s+', ' ', text.replace('\n', ' ').replace('\"', '"')).strip()
    return [cleaned_text[i:i + CHUNK_SIZE] for i in range(0, len(cleaned_text), CHUNK_SIZE)]

def process_md_files(folder_path):
    chunks = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                chunks.extend([(filename, chunk) for chunk in clean_and_chunk_text(file.read())])
    return chunks

def get_risk_info(json_data):
    risk_info = {}
    for item in json_data:
        code = item.get("Code", "")
        risk_info[code] = {
            "category": item.get("Risk Category", ""),
            "descriptions": {
                1: item.get("Strong", ""),
                2: item.get("Adequate", ""),
                3: item.get("Weak", "")
            }
        }
    return risk_info

def generate_assessment(chunk, code, category, descriptions):
    context = f"Context: {chunk}\nCode: {code}\nCategory: {category}\n"
    instruction = "Assess the risk level based on the context. The risk levels are:\n"
    for score, desc in descriptions.items():
        instruction += f"Score {score}: {desc}\n"

    full_instruction = f"[INST] Given the context '{context}' and considering the Risk Category '{category}', assess the risk level for code '{code}'. Provide the most directly related Risk Category as the Score (1, 2, or 3) and include the corresponding Risk Description. Make sure your response is specific and accurate. [/INST]"

    url = "http://localhost:8110/generate/"
    payload = {"context": full_instruction}
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            # Process and return the response
            response_text = response.json()[0]['generated_text']
            response_text.replace(full_instruction, "").strip()
            # Split the response into sentences
            sentences = re.split(r'(?<=[.!?])\s+', response_text)
            
            # Remove duplicated sentences
            unique_sentences = []
            for sentence in sentences:
                if sentence not in unique_sentences:
                    unique_sentences.append(sentence)
            
            # Join the unique sentences back into a single string
            unique_response = ' '.join(unique_sentences)
            unique_response = re.sub(r'<s>.*</>', '', unique_response)
            # print("response from llama",unique_response.replace(full_instruction, "").strip(), " end\n")
            
            return unique_response.replace(full_instruction, "").strip()
        else:
            return "Error in LLM response"
    except requests.RequestException as e:
        return str(e)

def parse_llm_output(assessment):
    # Adjusted regex pattern to match the LLM's output format
    pattern = r"Risk Level:\s*(\d)"

    matches = re.findall(pattern, assessment)
    if matches:
        # Assuming the first match is the relevant one
        parsed_score = int(matches[0])  # Score as an integer
        # Determine the corresponding risk description
        if parsed_score == 3:
            parsed_risk = "Strong"
        elif parsed_score == 2:
            parsed_risk = "Adequate"
        elif parsed_score == 1:
            parsed_risk = "Weak"
        else:
            parsed_risk = "Mitigating Control level not identified"
    else:
        parsed_score = None
        parsed_risk = "Mitigating Control level not identified"

    print(parsed_risk,parsed_score)

    return parsed_risk, parsed_score

def keyword_match(chunk, description):
    return any(word in chunk for word in description.split())

def assess_risk_with_llm(risk_info, md_chunks):
    risk_scores = {'Strong': 3, 'Adequate': 2, 'Weak': 1}
    output_data = []

    for code, info in risk_info.items():
        for doc_name, chunk in md_chunks:
            assessment = generate_assessment(chunk, code, # In the `assess_risk_with_llm` function,
            # `info` is a dictionary that contains
            # information about a specific risk code. It
            # is obtained from the `risk_info`
            # dictionary, which is generated from the
            # JSON input data.
            info["category"], info["descriptions"])

            # Parse the LLM output to get risk and score
            parsed_risk, parsed_score = parse_llm_output(assessment)

            output_data.append({
                'Code': code,                   # links with the code for Inherent Risk and Mitigating Controls 
                'Risk': parsed_risk,            # Links with Low Risk, Moderate Risk or High Risk from InherentRisk.json
                'Score': parsed_score,          # LLM defines either 1, 2, 3. This is linked with parsed_risk
                'Risk Rationale': assessment,   # LLM response is here to provide the response to why it generated the Score.append()   
                'Document_Name': doc_name,      # Document cited
                'Context': chunk,               # Text that was used to resolve Risk Rational, and Score
                'Comments': ''                  # This is for manual entry by the user. In the UI, feedback is to be made for the LLM team to address.
            })
            # print(output_data)
            if(parsed_score != None):
                break
        else:
            # Append only if no context is found in any chunk
            output_data.append({
                'Code': code,
                'Risk': "Mitigating Control level not identified.",
                'Score': 0,
                'Risk Rationale': "No clear rationale due to lack of context.",
                'Document_Name': '',
                'Context': '',
                'Comments': f'No clear context provided for Code: {code}, Risk Category: {info["category"]}'
            })

    # Save the output to JSON after processing each chunk
    save_to_json(output_data, JSON_OUTPUT_PATH)

# Constants
CHUNK_SIZE = 500
MD_FOLDER_PATH = "/home/cr8dl-user/2920wall/2920_Bank_Procedures"
JSON_INPUT_PATH = "/home/cr8dl-user/2920wall/ra_folder/BSAMitigatingControls.json"
JSON_OUTPUT_PATH = "/home/cr8dl-user/2920wall/test_md_folder_response/2920Wall_RA_MC_Bank_1.json"

# print("1")
# Main execution
json_data = read_json(JSON_INPUT_PATH)
# print("2")
risk_info = get_risk_info(json_data)
# print("3")
md_chunks = process_md_files(MD_FOLDER_PATH)
# print("4")
output_data = assess_risk_with_llm(risk_info, md_chunks)
# print(output_data)