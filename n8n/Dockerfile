FROM n8nio/n8n

# Set timezone (optional)
ENV GENERIC_TIMEZONE="America/New_York"

# Install Python and pip (Alpine-compatible syntax)
USER root
RUN apk add --no-cache python3 py3-pip
USER node

# Copy voicegen.py into container
COPY voicegen.py /app/voicegen.py

# Set permissions (just in case)
RUN chmod +x /app/voicegen.py

EXPOSE 5678
