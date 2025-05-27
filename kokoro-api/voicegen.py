import sys
import shutil
from gradio_client import Client

# Set UTF-8 encoding for stdout
sys.stdout.reconfigure(encoding='utf-8')

# Get arguments from command line
text = sys.argv[1] # First argument: input text
voice = sys.argv[2] # Second argument: voice
speed = float(sys.argv[3]) # Third argument: speed (converted to float)

print(f"Received text: {text}")
print(f"Voice: {voice}")
print(f"Speed: {speed}")

# Connect to local Gradio server
client = Client("http://localhost:7860/")

# Generate speech using the API
result = client.predict(
text=text,
voice=voice,
speed=speed,
api_name="/generate_speech"
)

# Define output path
output_path = r"D:\output.mp3"

# Move the generated file
shutil.move(result[1], output_path)

# Print output path
print(output_path)