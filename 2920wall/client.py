'''
    /home/cr8dl-user/2920wall/client.py
'''

import subprocess
import requests
import json
import time

# Timer function
def print_elapsed_time(start_time, operation_name):
    elapsed_time = time.time() - start_time
    print(f"Time taken for {operation_name}: {elapsed_time:.2f} seconds")

def generate_text_from_source(source_type, source):
    """
    Generates text either by executing a Python script or sending a request to the LLM server.

    Args:
        source_type (str): Either 'script' or 'llm' to specify the source type.
        source (str): The source content (script or text) to generate text from.

    Returns:
        str: The generated text or an error message.
    """
    if source_type == 'script':
        try:
            completed_process = subprocess.run(['python', source], capture_output=True, text=True, check=True)
            return completed_process.stdout
        except subprocess.CalledProcessError as e:
            return f"Script execution error: {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"
    elif source_type == 'llm':
        url = "http://localhost:8110/generate/"
        try:
            response = requests.post(url, json={"context": source})
            response.raise_for_status()  # Raise an exception for HTTP errors
            try:
                response_json = response.json()
                return response_json[0]['generated_text']
            except json.JSONDecodeError as json_error:
                return f"JSON parsing error: {json_error}"
        except requests.exceptions.RequestException as e:
            return f"Network error: {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"
    else:
        return "Invalid source_type. Use 'script' or 'llm'."

def generate_text_from_string(text):
    """Generates text using the LLM from a given string."""
    start_time = time.time()  # Start timer
    result = generate_text_from_source('llm', text)  # Corrected the source_type
    print_elapsed_time(start_time, "LLM text generation")  # Print elapsed time
    return result

def generate_text_from_file(file_path):
    """Executes the Python script at the given file path."""
    start_time = time.time()  # Start timer
    try:
        #print("enter")
        completed_process = subprocess.run(['python', file_path], capture_output=True, text=True, check=True)
        print_elapsed_time(start_time, "Script execution")  # Print elapsed time
        return completed_process.stdout
    except subprocess.CalledProcessError as e:
        print_elapsed_time(start_time, "Script execution")  # Print elapsed time even if there's an error
        return f"An error occurred: {e}"

def main():
    choice = input("Enter '1' to ask a question, '2' to process a python file: ")

    if choice == '1':
        question = input("Enter your question or text: ")
        result = generate_text_from_string(question)
        if result is not None:
            print("Result from LLM:", result)
    elif choice == '2':
        file_path = input("Enter the path to the file: ")
        result = generate_text_from_file(file_path)
        if result is not None:
            print("Result from LLM:", result)
    else:
        print("Invalid choice. Please enter '1' or '2'.")

if __name__ == "__main__":
    main()
