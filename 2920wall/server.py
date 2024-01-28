'''
    /home/cr8dl-user/2920wall/server.py
'''
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from pydantic import BaseModel
import torch
import subprocess
import json
import sys
import os
sys.path.append('/home/cr8dl-user/2920wall')
from script_2920.inherentrisk import JSON_OUTPUT_PATH

# Define a request model
class TextGenerationRequest(BaseModel):
    context: str

# Initialize FastAPI app
app = FastAPI()

# Jinja2 Templates for HTML response
templates = Jinja2Templates(directory="templates")

# Initialize and load model
device = "cuda" if torch.cuda.is_available() else "cpu"
model_name = "sajjadalik442/Llama-2-7b-chat-finetune-ffiec-finetuned"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to(device)
text_gen_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0 if device == "cuda" else -1)

@app.get("/")
async def root():
    return {"message": "Hello, this is the root of my FastAPI application!"}

# Define endpoint for text generation
@app.post("/generate/")
async def generate_text(request: TextGenerationRequest):
    try:
        generation = text_gen_pipeline(request.context, max_length=3000#, max_new_tokens=2048
                                        , num_return_sequences=1)
        return generation
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/run-script/")
async def run_script(request: Request):
    form_data = await request.form()
    script_name = form_data.get("script_name")

    # Construct the full path to the script
    script_path = f'/home/cr8dl-user/2920wall/{script_name}'

    try:
        # Run the Python script and capture its output
        completed_process = subprocess.run(['python', script_path], capture_output=True, text=True, check=True)
        output = completed_process.stdout

        # Save output to JSON file
        output_path = JSON_OUTPUT_PATH
        with open(output_path, 'w') as file:
            json.dump({'output': output}, file)

        return HTMLResponse(f"Script {script_name} executed. Output saved to {output_path}")

    except subprocess.CalledProcessError as e:
        return HTMLResponse(f"An error occurred: {e}")
    
# Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8110)
