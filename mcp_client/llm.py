import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class LLM:

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1",
        )

        self.model = os.getenv(
            "MODEL",
            "google/gemini-2.5-flash"
        )

    def chat(self, messages, tools=None):

        params = {
        "model": self.model,
        "messages": messages,
        "max_tokens": 512,
        "temperature": 0.3,
        }

        if tools:
            params["tools"] = tools
            params["tool_choice"] = "auto"

        return self.client.chat.completions.create(
            **params
        )
