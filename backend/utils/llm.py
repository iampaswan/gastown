
import requests

def llm_stream(prompt: str):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen2.5:3b",
            "prompt": prompt,
            "stream": True
        },
        stream=True
    )

    for line in response.iter_lines():
        if line:
            chunk = line.decode("utf-8")
            print(f"Steaming chunk: {chunk}")
            yield chunk

