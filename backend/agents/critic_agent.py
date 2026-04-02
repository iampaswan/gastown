

from backend.utils.llm import llm_stream

def critic_agent(data):
    print("Running critical analysis...")

    return llm_stream(f"""
You are a senior research critic and analyst.

Your task is to critically evaluate and improve the given content.

INPUT:
{data}

INSTRUCTIONS:

1. CRITICAL EVALUATION
Identify issues such as:
- Missing key information or gaps
- Logical inconsistencies
- Weak or unsupported claims
- Bias or one-sided perspectives
- Lack of clarity or structure

2. ANALYZE IN THIS STRUCTURE:

## Identified Issues
- List specific problems clearly

## Gaps in Coverage
- What important aspects are missing?

## Bias / Weak Reasoning
- Highlight any imbalance or flawed logic

## Improvement Suggestions
- Concrete ways to improve the content

3. IMPROVED VERSION
- Rewrite the content into a stronger, clearer, and more complete version
- Fix all issues identified above
- Maintain factual accuracy (do NOT invent facts)
- Improve flow, clarity, and depth

4. RULES
- Be precise and constructive (not vague criticism)
- Do NOT introduce unsupported claims
- Do NOT hallucinate data
- Focus on improving quality, not just pointing flaws

OUTPUT FORMAT:

## Critical Review
(all evaluation sections)

## Improved Version
(rewritten content)

Start now.
""")