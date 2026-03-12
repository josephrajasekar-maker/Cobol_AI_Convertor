from openai import OpenAI
from prompt_templates import COBOL_TO_PYTHON_PROMPT
import os
#load_dotenv()



client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def translate_cobol_to_python(cobol_code):

    prompt = f"""
Convert the following COBOL program to Python.

COBOL CODE:
{cobol_code}
"""
    try:

         response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
            {"role": "user", "content": prompt},
        
         ],
             temperature=0
        )   
          
        return response.choices[0].message.content

    except Exception as e:

        print("AI translation failed:", e)
        return "# AI translation failed"
