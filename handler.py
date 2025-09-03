import os
import runpod

IMPL = os.getenv("HANDLER_IMPL", "echo")

def echo_handler(job):
    """Lightweight: returns whatever you send, no heavy deps."""
    return {
        "ok": True,
        "impl": "echo",
        "input": job.get("input", {})
    }

# Lazy import so we don't pull transformers unless requested
_pipeline = None
def sentiment_handler(job):
    global _pipeline
    if _pipeline is None:
        from transformers import pipeline  # imported only when used
        cache_dir = os.getenv("HF_HOME", "/tmp/hf")  # works without a volume
        _pipeline = pipeline("sentiment-analysis", cache_dir=cache_dir)
    text = job.get("input", {}).get("text", "Hello RunPod")
    return {"impl": "sentiment", "result": _pipeline(text)}

HANDLERS = {"echo": echo_handler, "sentiment": sentiment_handler}
handler = HANDLERS.get(IMPL, echo_handler)

if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})
