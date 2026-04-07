from backend.utils.llm import llm_stream

def backend_node_agent(query: str):
    prompt = f"""
You are a senior backend engineer.

Create a Node.js backend using:
- TypeScript
- Express.js

For:
{query}

Rules:
- Return COMPLETE working code
- No missing values
- No placeholders like TODO or undefined
- Use best practices
- Include all imports
- Use proper TypeScript types
- Include app setup and server start
- Use modular structure if needed
- Include basic error handling
- Ensure code is executable

Project should include:
- Express app
- Routes
- Controllers (if needed)
- Middleware (if needed)
- Type definitions
- Port configuration

Wrap output STRICTLY like:

```typescript
// code here
"""
    
    for text in llm_stream(prompt):
     yield text