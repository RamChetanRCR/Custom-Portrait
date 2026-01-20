import os
import requests
from dotenv import load_dotenv

load_dotenv()

class LLMClient:
    def __init__(self, model="meta-llama/llama-3.1-8b-instruct"):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY not found in environment.")

        self.model = model
        self.url = "https://openrouter.ai/api/v1/chat/completions"

        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            # These two are recommended by OpenRouter
            "HTTP-Referer": "http://localhost",  
            "X-Title": "AI Living Portrait Project"
        }

    def generate(self, prompt):
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
        }

        response = requests.post(self.url, headers=self.headers, json=payload, timeout=60)

        if response.status_code != 200:
            raise RuntimeError(f"OpenRouter API error: {response.status_code} - {response.text}")

        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
