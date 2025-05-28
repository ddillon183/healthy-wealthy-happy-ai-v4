from fastapi import FastAPI
from pydantic import BaseModel
import torchaudio
import time
from TTS.api import TTS
from pydub import AudioSegment
import os

app = FastAPI()

# ✅ Updated to use a multi-speaker, multilingual TTS model
tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False, gpu=False)

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
    output_wav = "output.wav"
    output_mp3 = "output.mp3"

    start_time = time.time()

    # Generate speech (can be float array, list of tensors, or tensor)
    wav_output = tts.tts(text=data.text, speaker=data.voice, language=data.language)

    # Ensure torch tensor format
    if isinstance(wav_output, list):
        wav = wav_output[0]
    elif hasattr(wav_output, 'unsqueeze'):
        wav = wav_output
    else:
        import torch
        wav = torch.tensor(wav_output)

    torchaudio.save(output_wav, wav.unsqueeze(0), 22050)

    # Convert WAV to MP3 using pydub
    sound = AudioSegment.from_wav(output_wav)
    sound.export(output_mp3, format="mp3")

    end_time = time.time()

    os.remove(output_wav)

    return {
        "message": f"Generated speech saved as {output_mp3}",
        "file": output_mp3,
        "voice": data.voice,
        "language": data.language,
        "start": round(start_time, 3),
        "end": round(end_time, 3),
        "duration_seconds": round(end_time - start_time, 2)
    }





