import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GROQ_API_KEY: str = os.environ.get("GROQ_API_KEY")
    MODEL_NAME: str = "meta-llama/llama-4-maverick-17b-128e-instruct"
    API_V1_STR: str = "/api"
    PROJECT_NAME: str = "Chess Parser API"
    BACKEND_CORS_ORIGINS: list = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://localhost:8001",
        "https://chess-parser.vercel.app/",
    ]

    # Parse CORS origins from env if present
    _cors_origins_str = os.environ.get("BACKEND_CORS_ORIGINS")
    if _cors_origins_str:
        BACKEND_CORS_ORIGINS = [origin.strip() for origin in _cors_origins_str.split(",")]

settings = Settings()
