
from backend.utils.llm import llm_stream


def summarizer_agent(data, mode="standard"):
    if mode == "short":
        instruction = "Give a very concise summary (3-5 bullets)."
    elif mode == "deep":
        instruction = "Provide detailed structured summary with insights."
    else:
        instruction = "Provide a balanced structured summary."

    return llm_stream(f"""
You are an expert summarizer.

{instruction}

DATA:
{data}

Follow structured format with:
- Core Summary
- Key Facts
- Insights
""")