import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Use a lightweight transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

class InMemoryVectorStore:
    def __init__(self):
        self.docs = []
        self.index = None
        self.embeddings = None

    def build_index(self, documents):
        self.docs = documents
        self.embeddings = model.encode(documents)
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(np.array(self.embeddings))

    def query(self, query_text, top_k=3):
        if self.index is None:
            raise ValueError("Vector index is not initialized.")
        query_embedding = model.encode([query_text])
        distances, indices = self.index.search(np.array(query_embedding), top_k)
        return [self.docs[i] for i in indices[0] if i < len(self.docs)]
