# Stage 1: Base with Python
FROM python:3.11-slim as python-stage

# Install required packages
RUN pip install --no-cache-dir requests

# Copy the script
COPY voicegen.py /app/voicegen.py

# Stage 2: n8n base
FROM n8nio/n8n

# Copy Python, pip, and script from previous stage
COPY --from=python-stage /usr/local/bin/python3 /usr/local/bin/python3
COPY --from=python-stage /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=python-stage /usr/local/bin/pip3 /usr/local/bin/pip3
COPY --from=python-stage /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=python-stage /app/voicegen.py /app/voicegen.py

# Make sure the file is executable
RUN chmod +x /app/voicegen.py

# Set timezone
ENV GENERIC_TIMEZONE="America/New_York"

EXPOSE 5678
