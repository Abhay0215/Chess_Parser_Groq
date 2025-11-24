# Chess Parser Backend (Groq) 🧠

The high-performance backend for the Chess Parser application, powered by **FastAPI** and **Groq AI**. This service handles the complex task of interpreting chess scoresheet images and converting them into valid PGN moves.

## ✨ Features

-   **AI-Powered Extraction**: Utilizes [Groq's](https://groq.com/) LPU inference engine for lightning-fast text extraction and move interpretation.
-   **Intelligent Parsing**: Custom logic to clean and format OCR output into standard algebraic notation.
-   **Move Validation**: Integrated with `python-chess` to ensure all extracted moves are legal and valid in the game context.
-   **FastAPI Framework**: Built on modern, high-performance Python web framework standards.
-   **CORS Support**: Configured for seamless integration with the React frontend.

## 🛠️ Tech Stack

-   **Language**: [Python 3.8+](https://www.python.org/)
-   **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
-   **Server**: [Uvicorn](https://www.uvicorn.org/)
-   **AI/LLM**: [Groq SDK](https://github.com/groq/groq-python)
-   **Chess Logic**: [python-chess](https://python-chess.readthedocs.io/)

## 🚀 Getting Started

### Prerequisites

-   Python 3.8 or higher
-   A Groq API Key (Get one at [console.groq.com](https://console.groq.com))

### Installation

1.  Navigate to the backend directory:
    ```bash
    cd chess_parser/backend_groq
    ```

2.  Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3.  Activate the virtual environment:
    *   **Windows**:
        ```bash
        .\venv\Scripts\activate
        ```
    *   **Linux/Mac**:
        ```bash
        source venv/bin/activate
        ```

4.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1.  Create a `.env` file in the `backend_groq` directory (copy from `.env.example` if available).
2.  Add your Groq API key:
    ```env
    GROQ_API_KEY=gsk_your_actual_api_key_here
    ```

## 🏃 Running the Application

### Option 1: Quick Start (Windows)

Simply run the included batch file:
```bash
.\start_groq.bat
```
This script automatically sets up the environment and starts the server.

### Option 2: Manual Start

With your virtual environment activated:
```bash
python -m uvicorn main:app --reload --port 8001
```

The server will start at `http://localhost:8001`.

### Option 3: Docker (Recommended for Deployment) 🐳

You can containerize the application using Docker.

**Using Docker Compose:**

1.  Ensure you have Docker and Docker Compose installed.
2.  Make sure your `.env` file is configured.
3.  Run:
    ```bash
    docker-compose up --build
    ```

**Using Dockerfile manually:**

1.  Build the image:
    ```bash
    docker build -t chess-parser-backend .
    ```
2.  Run the container:
    ```bash
    docker run -p 8001:8001 --env-file .env chess-parser-backend
    ```

## 🔌 API Endpoints

### `POST /api/extract`

Extracts chess moves from an uploaded image.

-   **URL**: `/api/extract`
-   **Method**: `POST`
-   **Content-Type**: `multipart/form-data`

**Parameters:**

| Name | Type | Description |
| :--- | :--- | :--- |
| `file` | `File` | The image file of the chess scoresheet. |

**Success Response (200 OK):**

```json
{
  "moves": ["e4", "e5", "Nf3", "Nc6"],
  "fen": "r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3",
  "raw_text": "1. e4 e5 2. Nf3 Nc6 ...",
  "parsed_text": "e4 e5 Nf3 Nc6"
}
```

## 📂 Project Structure

```
backend_groq/
├── app/
│   ├── api/
│   │   └── routes.py          # API route definitions
│   ├── core/
│   │   └── config.py          # App configuration & settings
│   ├── services/
│   │   └── groq_service.py    # Groq AI integration logic
│   └── utils/
│       └── chess_utils.py     # Chess move validation helpers
├── main.py                    # Application entry point
├── requirements.txt           # Python dependencies
├── start_groq.bat             # Windows startup script
└── test_groq_backend.py       # Backend test script
```

## 🧪 Testing

To run the backend tests:

```bash
python test_groq_backend.py
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

[MIT](LICENSE)
