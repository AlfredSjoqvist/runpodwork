FROM python:3.10-slim
WORKDIR /app

# Install your model’s dependencies
RUN apt-get update && apt-get install -y git curl && rm -rf /var/lib/apt/lists/*

# Core RunPod SDK
RUN pip install --no-cache-dir runpod torch torchvision transformers

COPY handler.py /app/handler.py

CMD ["python3", "-u", "/app/handler.py"]
