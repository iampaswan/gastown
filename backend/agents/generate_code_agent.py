
from backend.utils.llm import llm_stream

def generate_code_agent(query: str):
    prompt = f"""
You are an expert programmer.

Task:
{query}


Rules:
- Return COMPLETE working code
- No missing values
- No placeholders like status_code=
- Include imports
- Ensure code is executable
- Wrap response in triple backticks

Wrap output STRICTLY like:

```
# code here

"""

    for text in llm_stream(prompt):
        yield text