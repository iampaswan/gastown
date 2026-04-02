import json


def create_convoy(query: str):
    query_lower = query.lower()

    convoy = []
    print("Creating convoy for query:", query)

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


    planning_prompt = f"""
You are a task planner.

Break this query into steps using available agents:

Agents:
- research_agent
- summarizer_agent
- critic_agent
- writer_agent

Return JSON list like:
[
  {{ "type": "research", "input": "..." }},
  ...
]

Query:
{query}
"""

    plan = call_llm(planning_prompt) 
    convoy = json.loads(plan)

    return convoy