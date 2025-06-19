from ai_rag.faiss_store import InMemoryVectorStore

def test_faiss_retrieval():
    store = InMemoryVectorStore()
    docs = ["client called to cancel", "final notice sent"]
    store.build_index(docs)
    result = store.query("cancel", top_k=1)
    assert any("cancel" in doc.lower() for doc in result)
