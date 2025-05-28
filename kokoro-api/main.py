from fastapi import FastAPI
from pydantic import BaseModel
import torchaudio
import time
from TTS.api import TTS

app = FastAPI()

# Load model
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

class SpeechRequest(BaseModel):
    text: str
    voice: str = "default"
    speed: float = 1.0
    language: str = "en"

@app.get("/voices")
async def get_voices():
    voices = tts.speakers if tts.speakers else ["default"]
    languages = tts.languages if tts.languages else ["en"]
    return {"voices": voices, "languages": languages}

@app.post("/speak")
async def speak(data: SpeechRequest):
    output_path = "output.wav"

    # Generate speech and duration
    start_time = time.time()
    wav = tts.tts(text=data.text, speaker=data.voice, language=data.language)
    end_time = time.time()

    # Save the file
    torchaudio.save(output_path, wav.unsqueeze(0), 22050)

    return {
        "message": f"Generated speech saved as {output_path}",
        "voice": data.voice,
        "language": data.language,
        "start": start_time,
        "end": end_time,
        "duration_seconds": round(end_time - start_time, 2)
    }
