
from utils.github import create_pr

repo = "iampaswan/RAG_chatbot_ai"   
title = "Testing PR"
body = "Testing meow"
token = "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"


response = create_pr(repo, title, body, token)

print(response)