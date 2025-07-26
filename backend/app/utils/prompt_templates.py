# prompt_templates.py
"""
Centralized prompt templates for the Insurance LLM System.
These prompts are designed for:
1. Query Parsing
2. Decision Making
3. Explainability
"""

### 1. Query Parsing Prompt ###
QUERY_PARSING_PROMPT = """
You are an intelligent assistant that extracts structured information from an insurance-related query.
Input Query: "{query}"

Extract the following details if available:
- age (integer)
- gender (male/female)
- procedure (like knee surgery, heart operation)
- location (city name)
- policy_duration (in months or days)
- any other relevant info

Output JSON in this format:
{
    "age": <int or null>,
    "gender": "<male/female or null>",
    "procedure": "<procedure or null>",
    "location": "<city or null>",
    "policy_duration": "<duration or null>"
}
"""

### 2. Decision Making Prompt ###
DECISION_PROMPT = """
You are an expert insurance decision assistant.
Analyze the user query and relevant policy clauses to decide APPROVAL or REJECTION.

User Query: "{query}"
Parsed Details: {structured_data}

Relevant Policy Clauses:
{clauses}

Task:
- Determine if the claim is Approved or Rejected.
- Estimate payout amount if applicable.
- Justify the decision by referencing the exact clauses used.

Output ONLY in valid JSON format like this:
{
    "decision": "Approved" or "Rejected",
    "amount": "<payout amount or N/A>",
    "justification": [
        {"clause": "<exact clause text>", "source": "<document name or ID>"}
    ]
}
"""

### 3. Explainability (Clause Mapping) ###
EXPLAINABILITY_PROMPT = """
You are an insurance auditor. Given the claim decision and retrieved policy clauses, explain the reasoning.

Decision: {decision}
User Query: "{query}"
Policy Clauses Used:
{clauses}

Output a human-readable explanation of why this decision was made.
"""
