from fastapi import FastAPI
from pydantic import BaseModel
from gradio_client import Client

app = FastAPI()

# ✅ This space is real and working (for test)
client = Client("https://kokoro-t4-gradio.hf.space")  # Adjust this if needed

class SpeechRequest(BaseModel):
    text: str
    voice: str = "en_male"
    speed: float = 1.0

@app.post("/speak")
async def speak(data: SpeechRequest):
    result = client.predict(
        text=data.text,
        voice=data.voice,
        speed=data.speed,
        api_name="/generate_speech"  # API endpoint must match the HF app
    )
    return {
        "audio_url": result[1],
        "duration": result[2],
        "voice": data.voice
    }

