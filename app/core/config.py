import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GROQ_API_KEY: str = os.environ.get("GROQ_API_KEY")
    MODEL_NAME: str = "meta-llama/llama-4-maverick-17b-128e-instruct"
    API_V1_STR: str = "/api"
    PROJECT_NAME: str = "Chess Parser API"

settings = Settings()
