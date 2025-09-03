import runpod
from transformers import pipeline

# Example: load a Hugging Face text classifier
classifier = pipeline("sentiment-analysis")

def handler(job):
    text = job["input"].get("text", "Hello RunPod")
    result = classifier(text)
    return {"input": text, "output": result}

if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})
