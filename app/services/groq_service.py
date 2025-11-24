from groq import Groq
import json
import base64
from app.core.config import settings

class GroqService:
    def __init__(self):
        self.client = Groq(api_key=settings.GROQ_API_KEY) if settings.GROQ_API_KEY else None

    async def extract_moves_from_image(self, image_content: bytes):
        if not self.client:
            raise Exception("GROQ_API_KEY not set")

        base64_image = base64.b64encode(image_content).decode('utf-8')
        
        try:
            completion = self.client.chat.completions.create(
                model=settings.MODEL_NAME,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Extract all chess moves from this scoresheet image. Return ONLY a JSON array of strings, e.g. [\"e4\", \"e5\", \"Nf3\"]. Do not include move numbers like '1.' or '2.'. Fix common OCR errors if possible."},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}"
                                }
                            }
                        ]
                    }
                ],
                temperature=0.1,
                max_completion_tokens=1024,
                top_p=1,
                stream=False,
                stop=None
            )
            
            result = completion.choices[0].message.content
            
            # Parse JSON
            try:
                start = result.find('[')
                end = result.rfind(']') + 1
                if start != -1 and end != -1:
                    json_str = result[start:end]
                    moves = json.loads(json_str)
                else:
                    moves = result.split()
            except:
                moves = result.split()
                
            return moves, result
            
        except Exception as e:
            raise Exception(f"Groq API Error: {str(e)}")

groq_service = GroqService()
