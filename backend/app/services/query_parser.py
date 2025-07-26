import openai
from services.prompt_templates import QUERY_PARSING_PROMPT

def parse_query_with_llm(query: str):
    prompt = QUERY_PARSING_PROMPT.format(query=query)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert query parser for insurance claims."},
            {"role": "user", "content": prompt}
        ]
    )

    return response["choices"][0]["message"]["content"]
