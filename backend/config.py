import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Updated working model
GROQ_MODEL = "llama-3.3-70b-versatile"

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./interview.db")
