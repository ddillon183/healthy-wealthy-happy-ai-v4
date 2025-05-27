FROM n8nio/n8n

USER root

# Install Python 3 and pip
RUN apt update && apt install -y python3 python3-pip

# Install Python packages
RUN pip install requests

# Copy your voice generation script into the container
COPY voicegen.py /app/voicegen.py

USER node
