import os
from pathlib import Path

from dotenv import load_dotenv


def load_api_key() -> str:
    env_path = Path(__file__).resolve().parent / ".env"
    load_dotenv(dotenv_path=env_path, override=False)

    api_key = os.getenv("GROQ_API_KEY", "").strip()

    if not api_key or api_key == "paste_your_groq_api_key_here":
        raise ValueError("Add your Groq API key to the .env file.")

    return api_key


if __name__ == "__main__":
    try:
        load_api_key()
    except ValueError as error:
        print(f"Configuration error: {error}")
        raise SystemExit(1)

    print("Configuration loaded successfully. API key is present.")