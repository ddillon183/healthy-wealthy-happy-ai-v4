from fastapi import FastAPI
from pydantic import BaseModel
from gradio_client import Client

app = FastAPI()

client = Client("https://matheusextra-kokoro.hf.space")

class SpeechRequest(BaseModel):
    text: str
    voice: str = "en_male"  # Optional default
    speed: float = 1.0      # Optional default

@app.post("/speak")
async def speak(data: SpeechRequest):
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
