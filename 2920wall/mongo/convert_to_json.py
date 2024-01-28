import PyPDF2
import json
import os

# PDF file path
pdf_file_path = "/home/cr8dl-user/2920wall/ml_training/252222333-Bank-Secrecy-Act-Anti-Money-Laundering-Examination-Manual-2014.pdf"

# Extract PDF file name without extension
pdf_file_name = os.path.splitext(os.path.basename(pdf_file_path))[0]

# JSON file path with the same name as the PDF
json_file_path = f"/home/cr8dl-user/2920wall/ml_training/{pdf_file_name}.json"

# Initialize a list to store the dictionaries
data_list = []

# Open the PDF file using PyPDF2's PdfReader
with open(pdf_file_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    # Iterate through pages and extract text
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        
        # Split the extracted text into lines
        lines = page_text.split('\n')
        
        # Process the lines and create dictionaries
        for line in lines:
            if line.strip():  # Check if the line is not empty
                data_dict = {
                    "name": pdf_file_name,  # Set the name to the PDF file name
                    "content": line.strip()  # Set the content to the line text
                }
                data_list.append(data_dict)

# Save the data as JSON with the same name as the PDF
with open(json_file_path, 'w') as json_output:
    json.dump(data_list, json_output, indent=4)

print("Conversion complete. JSON data saved to:", json_file_path)

# Example usage
# mongoimport --db 2920 --collection data --file /home/cr8dl-user/2920wall/ml_training/252222333-Bank-Secrecy-Act-Anti-Money-Laundering-Examination-Manual-2014.json --jsonArray

# View the data
# mongosh mongodb://localhost:27017/2920
# 2920> use 2920
# already on db 2920
# 2920> show collections
# 2920
# data
# 2920> db.data.find()