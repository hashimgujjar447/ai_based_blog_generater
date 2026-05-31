import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()


API_KEY=os.getenv("OPEN_ROUTER_API")

MODELS = [
    "openai/gpt-oss-120b:free",
    "openai/gpt-oss-20b:free",
    "meta-llama/llama-3.3-70b-instruct:free",
    "qwen/qwen3-next-80b-a3b-instruct:free",
    "google/gemma-4-31b-it:free",
    "google/gemma-4-26b-a4b-it:free"
]
def chat(messages,model):

        response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": model if model else  "google/gemma-4-31b-it:free",
            "messages": messages,
            "reasoning": {"enabled": True},
            
        }),
        timeout=60
        )

        return response.json()


