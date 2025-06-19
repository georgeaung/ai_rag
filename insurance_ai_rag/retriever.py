from insurance_ai_rag.faiss_store import InMemoryVectorStore

# Sample policy-to-documents map
document_map = {
    "12345": [
        "Client requested cancellation due to affordability issues.",
        "Customer was issued multiple payment reminders.",
        "Final cancellation notice sent on January 15th."
    ]
}

def retrieve_documents(policy_id):
    docs = document_map.get(policy_id, [])
    store = InMemoryVectorStore()
    store.build_index(docs)
    return store.query("why was the policy cancelled?")
