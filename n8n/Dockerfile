# Base image: Python with Node.js (for n8n)
FROM node:18-bullseye

# Set working directory
WORKDIR /app

# Install Python 3, pip, and n8n dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip build-essential git && \
    npm install -g n8n

# Install gradio client
RUN pip3 install gradio_client

# Copy your script
COPY voicegen.py /app/voicegen.py

# Set permissions (if needed)
RUN chmod +x /app/voicegen.py

# Set timezone for n8n
ENV GENERIC_TIMEZONE="America/New_York"

# Expose default n8n port
EXPOSE 5678

# Run n8n
CMD ["n8n"]
