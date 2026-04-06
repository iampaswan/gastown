

from backend.utils.llm import llm_stream
import json

def backendapi_agent(query: str):
    prompt = f"""
You are a senior backend engineer.

Create a FastAPI backend for the following requirement:

{query}

Requirements:
- Use FastAPI
- Include routes
- Use proper structure
- Return clean Python code
- No explanation, only code

"""

    for chunk in llm_stream(prompt):
        try:
            data = json.loads(chunk)
            text = data.get("response", "")

            if text:
                yield text

        except:
            continue