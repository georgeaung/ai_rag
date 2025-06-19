from insurance_ai_rag.snowflake_loader import get_policy_details
from insurance_ai_rag.retriever import retrieve_documents
from insurance_ai_rag.prompt import build_prompt
from insurance_ai_rag.llm import generate_response

def run_pipeline(policy_id):
    policy_data = get_policy_details(policy_id)
    docs = retrieve_documents(policy_id)
    prompt = build_prompt(policy_data, docs)
    return generate_response(prompt)
