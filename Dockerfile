FROM python:3.10-slim
WORKDIR /app

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONUNBUFFERED=1

# Minimal system deps; keep image small
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates && rm -rf /var/lib/apt/lists/*

# Required for serverless
RUN pip install --no-cache-dir runpod

# Your handler
COPY handler.py /app/handler.py

CMD ["python3", "-u", "/app/handler.py"]
