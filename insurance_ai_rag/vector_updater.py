import numpy as np
from insurance_ai_rag.faiss_store import InMemoryVectorStore
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
store = InMemoryVectorStore()

def update_vector_store(new_documents):
    if not new_documents:
        return
    new_embeddings = model.encode(new_documents)
    if store.embeddings is None:
        store.embeddings = np.array(new_embeddings)
        store.docs = new_documents
        store.index = store.index or InMemoryVectorStore().index
        store.index.add(store.embeddings)
    else:
        store.docs.extend(new_documents)
        store.embeddings = np.vstack([store.embeddings, new_embeddings])
        store.index.add(new_embeddings)
