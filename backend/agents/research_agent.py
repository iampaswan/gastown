
from backend.utils.llm import llm_stream

def research_agent(query):
    print(f"Researching topic: {query}")

    return llm_stream(f"""
You are a senior research analyst.

Conduct a deep, multi-perspective research analysis on the following topic:

TOPIC:
{query}

STRUCTURE:

## Overview (max 120 words)
## Key Findings (5–7 bullets, data-driven)
## Analysis (max 200 words)
## Recent Developments (max 120 words)
## Challenges (max 120 words)
## Conclusion (max 80 words)
## Sources (5–8 credible sources)

RULES:
- Total output must not exceed 1000 words
- No repetition across sections
- Use precise data and real sources only
- Be analytical, not verbose



""")



  #  prompts = [
  #                   f"Technical analysis of: {query}",
  #                   f"Economic and industry impact of: {query}",
  #                   f"Latest news and developments: {query}",
  #                   f"Academic research insights on: {query}"
  #                   ]
