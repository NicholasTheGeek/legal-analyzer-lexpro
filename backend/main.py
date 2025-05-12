from fastapi import FastAPI, Form
import requests

app = FastAPI()

# Centralized function for calling LLM
def call_llm(prompt: str) -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama2", "prompt": prompt, "stream": False}
    )
    response.raise_for_status()  # Ensure we handle errors properly
    return response.json().get("response", "").strip()

@app.post("/analyze/")
def analyze_legal(text: str = Form(...)):
    """Analyzes legal text for summaries, key clauses, and named entities."""
    prompts = {
        "summary": f"Summarize this legal document:\n\n{text}",
        "clauses": f"Extract key clauses from this legal text (e.g., Termination, Payment, Liability):\n\n{text}",
        "entities": f"Extract all named entities (e.g., parties, locations, dates):\n\n{text}"
    }

    # Ensuring LLM calls are safely executed
    results = {key: call_llm(prompt) for key, prompt in prompts.items()}
    return results