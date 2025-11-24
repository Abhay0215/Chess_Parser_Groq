import chess
import difflib

def get_closest_move(board, move_text):
    legal_moves = list(board.legal_moves)
    san_moves = [board.san(m) for m in legal_moves]
    
    # exact match
    if move_text in san_moves:
        return move_text
        
    # normalization (already done in main code, but good to have)
    move_text = move_text.replace('0', 'O')
    
    # Find closest match
    matches = difflib.get_close_matches(move_text, san_moves, n=1, cutoff=0.6)
    if matches:
        return matches[0]
    return None

def test_moves():
    moves = ['e4', 'e5', 'Nf3', 'Nb6', 'd3', 'd6', 'B04', 'Nf6', '0-0', 'Be6', 'Rfd8', 'de', 'd4', 'ed', 'Qxd4', 'Nc6', 'Qd2', 'a6']
    board = chess.Board()
    
    print(f"Testing {len(moves)} moves...")
    
    for i, move in enumerate(moves):
        try:
            board.push_san(move)
            print(f"{i+1}. {move} - OK")
        except ValueError:
            print(f"{i+1}. {move} - INVALID")
            # Try repair
            repaired = get_closest_move(board, move)
            if repaired:
                print(f"   -> Repaired: {repaired}")
                board.push_san(repaired)
            else:
                print("   -> Could not repair")

if __name__ == "__main__":
    test_moves()
