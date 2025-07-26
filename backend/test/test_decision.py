import pytest
import json
from app.services import decision_engine

# Mock response for LLM
MOCK_LLM_RESPONSE = """
{
    "decision": "Approved",
    "amount": "15000",
    "justification": [
        {"clause": "Knee surgery is covered under policy after 3 months", "source": "policy_doc_1"}
    ]
}
"""

@pytest.fixture
def sample_query():
    return "46-year-old male, knee surgery in Pune, 3-month-old insurance policy"

@pytest.fixture
def structured_data():
    return {
        "age": 46,
        "gender": "male",
        "procedure": "knee surgery",
        "location": "Pune",
        "policy_duration": "3 months"
    }

@pytest.fixture
def sample_clauses():
    return [
        {"text": "Knee surgery is covered under policy after 3 months", "source": "policy_doc_1"},
        {"text": "Pre-existing conditions not covered for 1 year", "source": "policy_doc_2"}
    ]


def test_make_decision(monkeypatch, sample_query, structured_data, sample_clauses):
    # Monkeypatch the OpenAI call
    def mock_openai_call(*args, **kwargs):
        class MockResponse:
            def __getitem__(self, item):
                return [{"message": {"content": MOCK_LLM_RESPONSE}}] if item == "choices" else None
        return MockResponse()

    # Patch the OpenAI API in decision_engine
    monkeypatch.setattr("app.services.decision_engine.openai.ChatCompletion.create", mock_openai_call)

    # Run the function
    response = decision_engine.make_decision(sample_query, structured_data, sample_clauses)

    # Validate JSON format
    try:
        result = json.loads(response)
    except json.JSONDecodeError:
        pytest.fail("Response is not valid JSON")

    assert result["decision"] == "Approved"
    assert result["amount"] == "15000"
    assert len(result["justification"]) > 0
    assert "Knee surgery" in result["justification"][0]["clause"]
