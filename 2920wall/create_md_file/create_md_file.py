import os
import pdfplumber
from docx import Document
import json
import re

from pandas import read_json

def read_pdf(file_path, start_page=4):
    """
    Reads the content of a PDF file and returns the text.
    """
    try:
        with pdfplumber.open(file_path) as pdf:
            text = ""
            for page_num in range(start_page - 1, len(pdf.pages)):  # Adjusted the page range
                page = pdf.pages[page_num]
                try:
                    # Specify encoding as 'utf-8'
                    page_text = page.extract_text(encoding='utf-8')
                    if page_text:
                        text += page_text
                except Exception as e:
                    # Handle any extraction errors
                    print(f"Error extracting text from page {page_num + 1}: {e}")
        return text
    except Exception as e:
        print(f"Error opening PDF file: {e}")
        return ""

def read_docx(file_path):
    """
    Reads the content of a DOCX file and returns the text.
    """
    doc = Document(file_path)
    return ' '.join([para.text for para in doc.paragraphs])

def convert_to_markdown(text):
    markdown = text
    
    # Convert headings
    markdown = re.sub(r'^(#+)(.*)', r'\1 \2', markdown, flags=re.MULTILINE)
    
    # Convert unordered lists
    markdown = re.sub(r'^\*\s+(.*)', r'- \1', markdown, flags=re.MULTILINE)
    
    # Convert ordered lists
    markdown = re.sub(r'^\d+\.\s+(.*)', r'1. \1', markdown, flags=re.MULTILINE)
    
    # Convert blockquotes
    markdown = re.sub(r'^>\s+(.*)', r'> \1', markdown, flags=re.MULTILINE)
    
    return markdown

def read_file(file_path, start_page=0):
    """
    Determines the file type and reads the content accordingly.
    """
    if file_path.endswith('.pdf'):
        return read_pdf(file_path, start_page)
    elif file_path.endswith('.docx'):
        return read_docx(file_path)
    elif file_path.endswith('.json'):
        return read_json(file_path)
    else:
        raise ValueError("Unsupported file type")

def extract_text_and_convert_to_markdown(input_file_path, output_dir, start_page=0):
    """
    Extracts text from the input file and converts it to Markdown.
    """
    # Read the content based on file type
    content = read_file(input_file_path, start_page)
    
    # Extract the base filename without extension
    base_filename = os.path.splitext(os.path.basename(input_file_path))[0]
    
    # Create the output file path with .md extension
    output_file_path = os.path.join(output_dir, f"{base_filename}.md")

    # Convert the text to Markdown
    markdown_output = convert_to_markdown(content)

    # Ensure the directory exists
    directory = os.path.dirname(output_file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Write the Markdown content to the output file
    with open(output_file_path, 'a') as md_file:
        md_file.write(markdown_output)

        print(f"Markdown content has been saved to {output_file_path}")

# Example usage:
input_file_path = '/home/cr8dl-user/2920wall/ml_training/ACAMS-Anti-Money-Laundering-Risk-Assessment-Methodology.pdf'
output_dir = '/home/cr8dl-user/2920wall/ml_training'
extract_text_and_convert_to_markdown(input_file_path, output_dir)
