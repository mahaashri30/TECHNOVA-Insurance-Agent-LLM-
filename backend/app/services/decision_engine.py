from services.prompt_templates import DECISION_PROMPT

def make_decision(query, structured_data, clauses):
    clause_text = "\n".join([f"- {c['text']} (Source: {c['source']})" for c in clauses])
    prompt = DECISION_PROMPT.format(query=query, structured_data=structured_data, clauses=clause_text)
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an insurance claim decision engine."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response["choices"][0]["message"]["content"]
