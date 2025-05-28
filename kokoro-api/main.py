from fastapi import FastAPI
from pydantic import BaseModel
from gradio_client import Client

app = FastAPI()

class SpeechRequest(BaseModel):
    text: str
    voice: str = "en_male"  # Default voice
    speed: float = 1.0      # Default speed

@app.post("/speak")
async def speak(data: SpeechRequest):
    try:
        # SAFELY initialize the Gradio client inside the function
        client = Client("https://matheusextra-kokoro.hf.space")

        result = client.predict(
            text=data.text,
            voice=data.voice,
            speed=data.speed,
            api_name="/generate_speech"
        )
        return {
            "audio_url": result[1],
            "duration": result[2],
            "voice": data.voice
        }

    except Exception as e:
        return {"error": str(e)}
