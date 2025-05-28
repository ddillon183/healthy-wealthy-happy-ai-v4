from fastapi import FastAPI
from pydantic import BaseModel
import gradio as gr
from TTS.api import TTS

app = FastAPI()

# Load default TTS model (you can change this later)
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

# Start Gradio in the background on launch
import threading
def run_gradio():
    def generate_speech(text, speaker="default", language="en"):
        file_path = "output.wav"
        tts.tts_to_file(text=text, file_path=file_path)
        return file_path
    interface = gr.Interface(fn=generate_speech, inputs=["text"], outputs="audio")
    interface.launch(server_name="0.0.0.0", server_port=7860, share=False)

threading.Thread(target=run_gradio).start()

# Define FastAPI schema
class SpeechRequest(BaseModel):
    text: str

@app.post("/speak")
async def speak(req: SpeechRequest):
    file_path = "output.wav"
    tts.tts_to_file(text=req.text, file_path=file_path)
    return {"message": "Generated speech saved as output.wav"}

@app.get("/voices")
async def get_voices():
    voices = tts.speakers if tts.speakers else ["default"]
    languages = tts.languages if tts.languages else ["en"]
    return {"voices": voices, "languages": languages}

