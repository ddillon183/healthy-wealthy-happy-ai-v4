from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SpeechRequest(BaseModel):
    text: str

@app.post("/speak")
async def speak(data: SpeechRequest):
    return {"message": f"Simulated voice for: {data.text}"}
