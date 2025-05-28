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

    # Generate speech (returns a list of tensors for multi-speaker models)
    wav_list = tts.tts(text=data.text, speaker=data.voice, language=data.language)

    # Convert to single tensor
    if isinstance(wav_list, list):
        import torch
        wav_tensor = torch.cat([t.unsqueeze(0) if len(t.shape) == 1 else t for t in wav_list], dim=1)
    else:
        wav_tensor = wav_list.unsqueeze(0)

    # Save to WAV
    torchaudio.save(output_wav, wav_tensor, 22050)

    # Convert WAV to MP3
    sound = AudioSegment.from_wav(output_wav)
    sound.export(output_mp3, format="mp3")

    end_time = time.time()

    # Clean up
    os.remove(output_wav)

    return {
        "message": f"Generated speech saved as {output_mp3}",
        "file": output_mp3,
        "voice": data.voice,
        "language": data.language,
        "start": start_time,
        "end": end_time,
        "duration_seconds": round(end_time - start_time, 2)
    }



