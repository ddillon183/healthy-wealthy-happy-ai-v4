import sys
import shutil
import os
from gradio_client import Client

# Read inputs
text = sys.argv[1]
voice = sys.argv[2]
speed = float(sys.argv[3])

print(f"Received text: {text}")
print(f"Voice: {voice}")
print(f"Speed: {speed}")

# Connect to Gradio server (running on port 7860 INSIDE the same container)
client = Client("http://adventurous-learning.railway.internal:7860/")

# Call Kokoro TTS
result = client.predict(
    text=text,
    voice=voice,
    speed=speed,
    api_name="/generate_speech"
)

# Define safe Linux-compatible path
output_path = "/app/output.mp3"

# Move the generated file
shutil.move(result[1], output_path)

print(f"Voice file saved to {output_path}")
