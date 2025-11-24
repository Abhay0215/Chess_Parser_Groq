import requests
import os

def test_backend():
    url = "http://localhost:8001/api/extract"
    image_path = "C:/Users/abhay/.gemini/antigravity/brain/e7e2ed47-dcb7-446b-abe4-bd167b507dee/uploaded_image_1763911820760.png"
    
    if not os.path.exists(image_path):
        print(f"Error: Image not found at {image_path}")
        return

    print(f"Testing backend at {url} with {image_path}...")
    
    try:
        with open(image_path, "rb") as f:
            files = {"file": f}
            response = requests.post(url, files=files)
            
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print("Response JSON:")
            print(data)
            if "moves" in data and len(data["moves"]) > 0:
                print("SUCCESS: Moves extracted!")
                import chess
                board = chess.Board()
                for i, move in enumerate(data["moves"]):
                    try:
                        board.push_san(move)
                        print(f"{i+1}. {move} - OK")
                    except Exception as e:
                        print(f"{i+1}. {move} - FAILED: {e}")
            else:
                print("WARNING: No moves returned.")
        else:
            print(f"Error: {response.text}")
            
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    test_backend()
