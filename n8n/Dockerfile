FROM n8nio/n8n

# Set working directory
WORKDIR /app

# Switch to root to install Python and dependencies
USER root

# Install Python and pip (Alpine-compatible)
RUN apk add --no-cache python3 py3-pip

# Install the gradio_client Python package
RUN pip install gradio_client

# Copy the voicegen script
COPY voicegen.py /app/voicegen.py

# Switch back to the default node user for security
USER node

# Set timezone
ENV GENERIC_TIMEZONE="America/New_York"

# Expose default n8n port
EXPOSE 5678
