
from backend.utils.llm import llm_stream

def research_agent(query):
    print(f"Researching topic: {query}")

    return llm_stream(f"""
You are a senior research analyst.

Conduct a deep, multi-perspective research analysis on the following topic:

TOPIC:
{query}

RESEARCH REQUIREMENTS:

1. COVERAGE
- Provide a comprehensive overview of the topic
- Include historical context and recent developments
- Cover multiple perspectives (economic, technological, social, geopolitical if relevant)

2. FACTUAL DEPTH
- Include verified facts and key statistics
- Mention specific data points, studies, or reports
- Avoid vague statements

3. SOURCE QUALITY
- Use high-quality sources such as:
  - Academic papers
  - Government reports
  - Reputable news organizations
  - Industry research (McKinsey, Gartner, etc.)

4. STRUCTURE YOUR OUTPUT AS:

## Overview
(detailed explanation)

## Key Findings
- bullet points with data

## Detailed Analysis
(in-depth explanation with reasoning)

## Recent Developments
(latest trends, updates)

## Challenges / Criticism
(balanced view)

## Conclusion
(clear takeaway)

## Sources
- List at least 5–10 credible sources
- Use realistic citation format:
  [1] Source name – title – year
  [2] Organization – report name – year

IMPORTANT RULES:
- Do NOT invent fake sources
- If unsure, say "limited data available"
- Be precise and analytical, not generic
- Prefer depth over length

Start now.
""")