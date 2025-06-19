from ai_rag.prompt import build_prompt

def test_build_prompt_format():
    policy_data = {
        "policy_id": "12345",
        "cancel_code": "NP",
        "payment_summary": "3 missed payments"
    }
    documents = ["Email from client about affordability", "Cancellation notice sent Jan 15"]
    prompt = build_prompt(policy_data, documents)
    assert "12345" in prompt and "affordability" in prompt
