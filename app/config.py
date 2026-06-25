import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")

OLLAMA_URL = os.getenv("OLLAMA_URL")

DATABASE_URL = os.getenv("DATABASE_URL")