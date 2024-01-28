"""
    Inherent Risk 
    
    Generates Risk Assessments for each code in the JSON file using a language model,
    and saves the output as a JSON file.
    
"""
import os
import json
import xmltodict
import xml.etree.ElementTree as ET
import re
import requests

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_to_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def dict_to_xml(data, root_tag="root"):
    root = ET.Element(root_tag)
    for key, value in data.items():
        if isinstance(value, dict):
            sub_element = ET.SubElement(root, key)
            for sub_key, sub_value in value.items():
                child = ET.SubElement(sub_element, sub_key)
                child.text = str(sub_value)
        else:
            child = ET.SubElement(root, key)
            child.text = str(value)
    return root

def pretty_print_xml(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            pretty_print_xml(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def save_to_xml(data, file_path):
    try:
        # Wrap the data in a root element
        xml_data = xmltodict.unparse({"root": {"item": data}}, pretty=True)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(xml_data)
    except Exception as e:
        print(f"Error in save_to_xml: {e}")
        
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
                1: item.get("Low Risk", ""),
                2: item.get("Moderate Risk", ""),
                3: item.get("High Risk", "")
            }
        }
    return risk_info

def generate_assessment(chunk, code, category, descriptions):
    context = f"Context: {chunk}\nCode: {code}\nCategory: {category}\n"
    instruction = "Assess the risk level based on the context. The risk levels are:\n"
    for score, desc in descriptions.items():
        instruction += f"Score {score}: {desc}\n"

    full_instruction = (
    "[INST] As a BSA/AML Auditor tasked with writing a risk assessment, your role is to evaluate the inherent risks of a bank based on its documentation. "
    "Each assessment should be precise and insightful, directly reflecting the bank's risk profile. "
    "Context: '{context}'. Risk Category: '{category}'. Code: '{code}'. "
    "Your task: Assess the risk level for the given code. "
    "Provide a score (1: Low Risk, 2: Moderate Risk, 3: High Risk) that most accurately reflects the risk in relation to the provided context and category. "
    "Include a concise risk description that is specific to the category and context, focusing on relevance and accuracy. "
    "Avoid redundancy and ensure your response is strictly pertinent to the assessment. [/INST]"
)

    url = "http://localhost:8110/generate/"
    payload = {"context": full_instruction}
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            # Process and return the response
            response_text = response.json()[0]['generated_text']
            # Remove the [INST]...[/INST] instruction part
            response_text = re.sub(r'\[INST\].*?\[/INST\]', '', response_text, flags=re.DOTALL).strip()

            # Split the response into sentences
            sentences = re.split(r'(?<=[.!?])\s+', response_text)
            
            # Remove duplicated sentences
            unique_sentences = list(dict.fromkeys(sentences))  # This removes duplicates
            
            # Join the unique sentences back into a single string
            unique_response = ' '.join(unique_sentences)
            unique_response = re.sub(r'<s>.*</>', '', unique_response)
            # print("response from llama",unique_response.replace(full_instruction, "").strip(), " end\n")
            
            return unique_response
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
        if parsed_score == 1:
            parsed_risk = "Low Risk"
        elif parsed_score == 2:
            parsed_risk = "Moderate Risk"
        elif parsed_score == 3:
            parsed_risk = "High Risk"
        else:
            parsed_risk = "Risk level not identified"
    else:
        parsed_score = None
        parsed_risk = "Risk level not identified"

    print(parsed_risk,parsed_score)

    return parsed_risk, parsed_score

def keyword_match(chunk, description):
    return any(word in chunk for word in description.split())

def aggregate_related_documents(output_data, code):
    """
    Aggregates related documents for a given risk code.

    Args:
        output_data (list): The list of output data entries.
        code (str): The risk code.

    Returns:
        tuple: Aggregated document names, contexts, and comments.
    """
    document_names = []
    contexts = []
    comments = []

    for entry in output_data:
        if entry['Code'] == code and entry['Risk'] != "Risk level not identified.":
            document_names.append(entry['Document_Name'])
            contexts.append(f"{entry['Document_Name']}:{entry['Context']}")
            comments.append(f"{entry['Document_Name']} - {entry['Risk Rationale']}")

    return ", ".join(document_names), "\n".join(contexts), "\n".join(comments)

def assess_risk_with_llm(risk_info, md_chunks):
    risk_scores = {'Low Risk': 1, 'Moderate Risk': 2, 'High Risk': 3}
    output_data = []

    for code, info in risk_info.items():
        # Temporary list to hold data for the current code
        temp_output_data = []
        risk_assessed = False
        for doc_name, chunk in md_chunks:
            assessment = generate_assessment(chunk, code,   # In the `assess_risk_with_llm` function, `info` is a dictionary that contains information about a specific risk code. 
                                                            # It is obtained from the `risk_info` dictionary, which is generated from the JSON input data.
                                            info["category"], info["descriptions"])

            # Parse the LLM output to get risk and score
            parsed_risk, parsed_score = parse_llm_output(assessment)

            temp_output_data.append({
                'Code': code,                   # links with the code for Inherent Risk and Mitigating Controls 
                'Risk': parsed_risk,            # Links with Low Risk, Moderate Risk or High Risk from InherentRisk.json
                'Score': parsed_score,          # LLM defines either 1, 2, 3. This is linked with parsed_risk
                'Risk Rationale': assessment,   # LLM response is here to provide the response to why it generated the Score.append()   
                'Document_Name': doc_name,      # Document cited
                'Context': chunk,               # Text that was used to resolve Risk Rational, and Score
                'Comments': ''                  # This is for manual entry by the user. In the UI, feedback is to be made for the LLM team to address.
            })
            if parsed_score is not None:
                risk_assessed = True
                break  # Exit loop once a risk is assessed

        if not risk_assessed:
            # Append only if no context is found in any chunk
            # Append only if no context is found in any chunk
            temp_output_data.append({
                'Code': code,
                'Risk': "Risk level not identified.",
                'Score': 0,
                'Risk Rationale': "No clear rationale due to lack of context.",
                'Document_Name': '',
                'Context': '',
                'Comments': f'No clear context provided for Code: {code}, Risk Category: {info["category"]}'
            })
        
        # Aggregate related documents
        aggregated_doc_names, aggregated_contexts, aggregated_comments = aggregate_related_documents(temp_output_data, code)

        # Update each entry with aggregated information
        for entry in temp_output_data:
            entry['Document_Name'] = aggregated_doc_names
            entry['Context'] = aggregated_contexts
            entry['Comments'] = aggregated_comments

        # Add the temporary data to the main output data
        output_data.extend(temp_output_data)

        # Save the output to JSON after processing each chunk
        save_to_json(output_data, JSON_OUTPUT_PATH)
        save_to_xml(output_data, XML_OUTPUT_PATH)

# Constants
CHUNK_SIZE = 500
MD_FOLDER_PATH = "/home/cr8dl-user/2920wall/2920_Bank_Procedures"
JSON_INPUT_PATH = "/home/cr8dl-user/2920wall/ra_folder/BSAInherentRisk.json"
JSON_OUTPUT_PATH = "/home/cr8dl-user/2920wall/test_md_folder_response/InherentRisk.json"
# Extract PDF file name without extension
json_file_name = os.path.splitext(os.path.basename(JSON_OUTPUT_PATH))[0]
print(f'json file name: {json_file_name}')
# XML file path with the same name as the JSON
XML_OUTPUT_PATH = f"/home/cr8dl-user/2920wall/test_xml/{json_file_name}.xml"
print(f'xml file name: {XML_OUTPUT_PATH}')

# Main execution
json_data = read_json(JSON_INPUT_PATH)
risk_info = get_risk_info(json_data)
md_chunks = process_md_files(MD_FOLDER_PATH)
output_data = assess_risk_with_llm(risk_info, md_chunks)
