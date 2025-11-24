@echo off
echo Setting up Groq Backend...
echo.

REM Check if venv exists, if not create it
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

REM Activate venv and install dependencies
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt --quiet

echo.
echo Starting Groq Backend Server on port 8001...
echo Press Ctrl+C to stop the server
echo.

python -m uvicorn main:app --reload --port 8001
