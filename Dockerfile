FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your agent code
COPY . .

# Environment variable to point to host's Ollama
ENV OLLAMA_BASE_URL="http://host.docker.internal:11434"

CMD ["python", "main.py"]