import chess
import difflib

def repair_move(board, move_text):
    """
    Attempts to repair an invalid move string by finding the closest legal move.
    """
    legal_moves = list(board.legal_moves)
    san_moves = [board.san(m) for m in legal_moves]
    
    # 1. Check for common OCR patterns
    if move_text in ['de', 'de5']:
        for m in san_moves:
            if m.startswith('dxe'): return m
    if move_text in ['ed', 'ed4']:
        for m in san_moves:
            if m.startswith('exd'): return m
    if '0' in move_text:
        # Try replacing 0 with c (common for Bc4 -> B04)
        candidate = move_text.replace('0', 'c')
        if candidate in san_moves: return candidate
        # Try replacing 0 with b
        candidate = move_text.replace('0', 'b')
        if candidate in san_moves: return candidate

    # 2. Fuzzy match against legal moves
    matches = difflib.get_close_matches(move_text, san_moves, n=1, cutoff=0.6)
    if matches:
        return matches[0]
        
    return None

def validate_moves(moves):
    """
    Validates a list of SAN moves and returns valid moves and the resulting FEN.
    Handles common OCR errors and partial move lists.
    """
    board = chess.Board()
    processed_moves = []
    
    for mv in moves:
        mv = str(mv).strip()
        if not mv: continue
        
        # Skip move numbers if they leaked through (e.g. "1.")
        if mv.endswith('.'): continue
        
        # Normalize castling (0-0 -> O-O)
        mv = mv.replace('0-0-0', 'O-O-O').replace('0-0', 'O-O')
        
        try:
            board.push_san(mv)
            processed_moves.append(mv)
        except:
            # Try to repair the move
            repaired = repair_move(board, mv)
            if repaired:
                board.push_san(repaired)
                processed_moves.append(repaired)
            else:
                # Keep invalid moves for display purposes, but don't play them
                # This might break the chain, but better than nothing
                processed_moves.append(mv)
                
    return processed_moves, board.fen()
