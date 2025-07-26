import pytest
import json
from app.services import query_parser

# Mocked LLM response for query parsing
MOCK_QUERY_PARSE_RESPONSE = """
{
    "age": 46,
    "gender": "male",
    "procedure": "knee surgery",
    "location": "Pune",
    "policy_duration": "3 months"
}
"""

@pytest.fixture
def sample_query():
    return "46-year-old male, knee surgery in Pune, 3-month-old insurance policy"

def test_parse_query(monkeypatch, sample_query):
    # Monkeypatch OpenAI API to return mock response
    def mock_openai_call(*args, **kwargs):
        class MockResponse:
            def __getitem__(self, key):
                return [{"message": {"content": MOCK_QUERY_PARSE_RESPONSE}}] if key == "choices" else None
        return MockResponse()

    # Patch the OpenAI call in query_parser
    monkeypatch.setattr("app.services.query_parser.openai.ChatCompletion.create", mock_openai_call)

    # Call the actual function
    response = query_parser.parse_query_with_llm(sample_query)

    # Validate that response is JSON and has required fields
    try:
        parsed_data = json.loads(response)
    except json.JSONDecodeError:
        pytest.fail("Query parsing response is not valid JSON")

    assert parsed_data["age"] == 46
    assert parsed_data["gender"] == "male"
    assert "knee surgery" in parsed_data["procedure"].lower()
    assert parsed_data["location"] == "Pune"
    assert "3" in parsed_data["policy_duration"]
