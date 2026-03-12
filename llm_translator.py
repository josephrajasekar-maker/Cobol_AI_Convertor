from openai import OpenAI
from prompt_templates import COBOL_TO_PYTHON_PROMPT
import os
#load_dotenv()



client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def translate_cobol_to_python(cobol_code):
    prompt = f"""Convert the following COBOL program to Python.
Step-by-step, analyze and explain how each section maps to Python, then provide the complete Python code.

COBOL CODE:
{cobol_code}
"""
    response = client.chat.completions.create(
        model="gpt-4",        # Use gpt-4 for best results
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=2048,
        temperature=0.1,
    )
    return response.choices[0].message.content
    #return response['choices'][0]['message']['content']
    
