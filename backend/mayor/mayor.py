import json
from backend.utils.llm import call_llm


def create_convoy(query: str):
    query_lower = query.lower()

    convoy = []
    print("Creating convoy for query:", query)


    if any(word in query.lower() for word in ["api", "backend", "server", "endpoint"]):
     return [
        {"type": "backend", "input": query}
    ]

    convoy.append({
        "type": "research",
        "input": query
    })

    if len(query.split()) > 3:
        convoy.append({
            "type": "summarize"
        })

    if "impact" in query_lower or "analysis" in query_lower:
        convoy.append({
            "type": "critic"
        })
        
    convoy.append({
        "type": "write"
    })



    print("Created convoy:", convoy)

    return convoy

