FROM n8nio/n8n:1.94.0

# Set timezone
ENV GENERIC_TIMEZONE="America/New_York"

# Install Python 3 and pip using Alpine package manager
USER root
RUN apk add --no-cache python3 py3-pip

# Switch back to node user for running n8n
USER node

EXPOSE 5678
