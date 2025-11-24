# Backend Groq - Virtual Environment Setup

# Create virtual environment
python -m venv venv

# Activate and install dependencies
.\venv\Scripts\activate
pip install -r requirements.txt

# Run the server
python -m uvicorn main:app --reload --port 8001
