FROM n8nio/n8n:1.94.0

# Set timezone (optional, but you're already using it)
ENV GENERIC_TIMEZONE="America/New_York"

# Install Python 3 and pip
USER root
RUN apt-get update && apt-get install -y python3 python3-pip

# Switch back to node user for n8n security
USER node

EXPOSE 5678
