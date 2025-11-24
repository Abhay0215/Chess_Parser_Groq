import chess
import random

class ChessEngine:
    """
    A placeholder chess engine service.
    Replace the logic in 'get_best_move' with your own model inference.
    """

    @staticmethod
    def get_best_move(fen: str) -> str:
        """
        Given a FEN string, returns the best move in UCI format (e.g., "e2e4").
        """
        board = chess.Board(fen)
        
        if board.is_game_over():
            return None

        # --- YOUR MODEL LOGIC GOES HERE ---
        # Example:
        # model_input = preprocess(fen)
        # move_index = model.predict(model_input)
        # move = decode_move(move_index)
        
        # For now, we just return a random legal move
        legal_moves = list(board.legal_moves)
        if not legal_moves:
            return None
            
        random_move = random.choice(legal_moves)
        return random_move.uci()

chess_engine = ChessEngine()
