import pytest
from ai_rag.pipeline import run_pipeline

def test_run_pipeline_contains_keywords():
    explanation = run_pipeline("12345")
    assert any(kw in explanation.lower() for kw in ["cancel", "termination", "non-payment"])
