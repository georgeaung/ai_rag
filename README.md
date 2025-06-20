# RAG AI Explainer For Data Governance - POC

This project is a Retrieval-Augmented Generation (RAG) system that POC following use cases 
- explains why insurance policies were cancelled early, combining:
- Generate  <company> approved project plan for implementing 16 weeks Master Data Management (MDM) implementation for a [industry] [company]

combining the followings: 

    - Structured data from Snowflake or other structured data respository
    - Unstructured documents from SharePoint/FileNet \n
    - GPT-4 based natural language generation \n
    - FAISS-based in-memory vector store for semantic retrieval \n

##  How FAISS Document Retrieval Works (FAISS for POC and PineCone or CosmoDB for production )

1. Documents linked to the policy are embedded using `sentence-transformers`.
2. Embeddings are indexed using FAISS `IndexFlatL2`.
3. A semantic query like "why was the policy cancelled?" is vectorized.
4. FAISS retrieves top-k matching chunks by similarity.

## Run Locally

```bash
uvicorn george_ai_rag.api:app --reload
```

Then test:

```json
POST /explain-cancellation/
{ "policy_id": "12345" }
```
