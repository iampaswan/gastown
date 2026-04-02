

from backend.utils.llm import llm_stream

def summarize_tool(data):
    print(f"Summarizing research data: {data}")
    return llm_stream(
        f"Summarize the following research into clear bullet points:\n\n{data}"
    )