from fastapi import FastAPI
from pydantic import BaseModel
from ai_rag.pipeline import run_pipeline
from ai_rag.scheduler import start_scheduler

app = FastAPI()

class PolicyRequest(BaseModel):
    policy_id: str

@app.on_event("startup")
def on_startup():
    start_scheduler()

@app.post("/explain-cancellation/")
def explain(request: PolicyRequest):
    return {"explanation": run_pipeline(request.policy_id)}
