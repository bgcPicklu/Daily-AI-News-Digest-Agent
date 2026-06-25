import requests
from app.config import OLLAMA_URL

def summarize(text):

    prompt = f"""
    Summarize in 3 bullet points:

    {text}
    """

    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model":"llama3.2",
            "prompt":prompt,
            "stream":False
        }
    )

    return response.json()["response"]