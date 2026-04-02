
from backend.utils.llm import llm_stream


def writer_agent(data):
    print("Writing intelligent report...")

    return llm_stream(f"""
You are a senior research writer and analyst.

Your task is to transform the provided material into a polished, professional, and insightful report.

INPUT:
{data}

INSTRUCTIONS:

1. UNDERSTAND BEFORE WRITING
- Do not copy-paste
- Synthesize information into a coherent narrative
- Identify key themes and relationships

2. STRUCTURE THE REPORT:

## Introduction
- Context and importance of the topic
- Brief overview

## Key Insights
- Clearly explained major findings
- Use bullet points where appropriate

## Detailed Analysis
- Expand on insights with reasoning
- Connect ideas logically

## Challenges / Limitations
- Risks, gaps, or criticisms

## Future Outlook
- Trends, predictions, opportunities

## Conclusion
- Clear and strong takeaway

3. WRITING STYLE
- Professional and analytical tone
- Clear, concise, and well-flowing paragraphs
- Avoid repetition
- Avoid generic filler phrases

4. CITATIONS
- Use inline citations like [1], [2] where relevant
- Base citations ONLY on provided data
- Do NOT invent new sources

5. QUALITY RULES
- Improve clarity and readability
- Ensure logical flow between sections
- Make the output feel like a human-written report

6. IMPORTANT
- Do NOT hallucinate facts
- Do NOT introduce new unsupported claims
- Stay faithful to input data

Generate a high-quality report now.
""")





