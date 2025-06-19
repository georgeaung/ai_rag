def build_prompt(policy_data, documents):
    doc_text = "\n".join(documents)
    return f"""
You are an insurance analyst.

Policy Summary:
- ID: {policy_data['policy_id']}
- Cancellation Reason Code: {policy_data['cancel_code']}
- Payment History: {policy_data['payment_summary']}

Documents:
{doc_text}

Why was the policy cancelled early?
"""
