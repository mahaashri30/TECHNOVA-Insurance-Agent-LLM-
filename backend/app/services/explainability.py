import json

def format_justification(raw_output: str):
    try:
        return json.loads(raw_output)
    except:
        # Fallback if LLM output isn't valid JSON
        return {"decision": "Error", "amount": "N/A", "justification": []}
