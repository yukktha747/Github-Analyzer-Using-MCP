import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    BASE_URL = "https://api.github.com"

    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

    CACHE_DURATION = int(
        os.getenv("CACHE_DURATION", 600)
    )

    LOG_LEVEL = os.getenv(
        "LOG_LEVEL",
        "INFO"
    )

    REQUEST_TIMEOUT = 10

    HEADERS = {
        "Accept": "application/vnd.github+json"
    }

    if GITHUB_TOKEN:
        HEADERS["Authorization"] = (
            f"Bearer {GITHUB_TOKEN}"
        )