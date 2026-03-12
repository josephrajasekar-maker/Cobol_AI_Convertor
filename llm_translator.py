from openai import OpenAI
from prompt_templates import COBOL_TO_PYTHON_PROMPT

client = OpenAI()
export OPENAI_API_KEY= "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"

def translate_cobol_to_python(cobol_code):

    prompt = COBOL_TO_PYTHON_PROMPT.format(
        cobol_code=cobol_code
    )

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content
