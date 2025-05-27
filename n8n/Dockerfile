# Stage 1: Build with Python and install packages
FROM python:3.11-slim as python-stage

# Install the gradio_client
RUN pip install --no-cache-dir gradio_client

# Copy the voicegen script
COPY voicegen.py /app/voicegen.py

# Stage 2: n8n base
FROM n8nio/n8n

# Copy Python runtime, site-packages, and script from Python stage
COPY --from=python-stage /usr/local/bin/python3 /usr/local/bin/python3
COPY --from=python-stage /usr/local/bin/pip3 /usr/local/bin/pip3
COPY --from=python-stage /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=python-stage /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=python-stage /app/voicegen.py /app/voicegen.py

# Set timezone
ENV GENERIC_TIMEZONE="America/New_York"

EXPOSE 5678
