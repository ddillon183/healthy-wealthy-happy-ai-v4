from fastapi import FastAPI
from pydantic import BaseModel
from gradio_client import Client

app = FastAPI()

# Reliable TTS endpoint for Kokoro on HuggingFace
client = Client("https://kokoro-tts.hf.space")

class SpeechRequest(BaseModel):
    text: str
    voice: str = "en_male"
    speed: float = 1.0

@app.post("/speak")
async def speak(data: SpeechRequest):
    try:
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
