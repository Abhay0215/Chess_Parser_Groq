from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.groq_service import groq_service
from app.utils.chess_utils import validate_moves

router = APIRouter()

@router.get("/")
async def root():
    return {
        "status": "ok",
        "message": "Chess Parser Backend is running",
        "version": "2.0",
        "endpoints": ["/extract", "/engine/move"]
    }


@router.post("/extract")
async def extract_moves(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        
        # Extract moves using Groq
        moves, raw_text = await groq_service.extract_moves_from_image(contents)
        
        # Validate and process moves
        processed_moves, fen = validate_moves(moves)
        
        return {
            "moves": processed_moves,
            "fen": fen,
            "raw_text": raw_text,
            "parsed_text": " ".join(processed_moves)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

from pydantic import BaseModel

class EngineMoveRequest(BaseModel):
    fen: str

@router.post("/engine/move")
async def get_engine_move(request: EngineMoveRequest):
    from app.services.chess_engine import chess_engine
    try:
        move = chess_engine.get_best_move(request.fen)
        return {"move": move}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
