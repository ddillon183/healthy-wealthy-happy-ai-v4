FROM n8nio/n8n

# Set working directory
WORKDIR /app

# Switch to root to install Python and copy files
USER root

# Install Python and pip
RUN apk add --no-cache python3 py3-pip

# Copy the voicegen script
COPY voicegen.py /app/voicegen.py

# Make the script executable (optional now)
# RUN chmod +x /app/voicegen.py

# Switch back to the default non-root user for security
USER node

# Set timezone for n8n
ENV GENERIC_TIMEZONE="America/New_York"

# Expose default n8n port
EXPOSE 5678
