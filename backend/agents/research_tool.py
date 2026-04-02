

from backend.utils.llm import llm_stream

def research_tool(query):
    print(f"Researching topic: {query}")
    return llm_stream(
        f"Do deep research on the topic: {query}. Include key facts, trends, and examples."
    )