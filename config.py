import os
from dotenv import load_dotenv

# .env ফাইল থেকে ডেটা লোড করা
load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    META_ACCESS_TOKEN = os.getenv("META_ACCESS_TOKEN")
    TIKTOK_ACCESS_TOKEN = os.getenv("TIKTOK_ACCESS_TOKEN")