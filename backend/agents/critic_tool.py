

from backend.utils.llm import llm_stream

def critic_tool(data):
    print(f"Critically evaluating summary: {data}")
    return llm_stream(
        f"Critically evaluate the following summary. Highlight any gaps or biases and improve it:\n\n{data}"
    )