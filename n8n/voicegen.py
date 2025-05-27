import sys
import requests

# Get command-line arguments
text = sys.argv[1]
voice = sys.argv[2]
speed = float(sys.argv[3])

print(f"🗣️ Sending text: {text} | Voice: {voice} | Speed: {speed}")

# Construct the POST request
url = "http://adventurous-learning.railway.internal:8000/speak"
payload = {
    "text": text,
    "voice": voice,
    "speed": speed
}

# Send request to Kokoro FastAPI server
response = requests.post(url, json=payload)

if response.ok:
    with open("/app/output.mp3", "wb") as f:
        f.write(response.content)
    print("✅ Audio saved as output.mp3")
else:
    print(f"❌ Error {response.status_code}: {response.text}")
