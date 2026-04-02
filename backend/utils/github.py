import requests
import os

import requests

def create_pr(repo, title, body, token):
    url = f"https://api.github.com/repos/{repo}/pulls"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    data = {
        "title": title,
        "body": body,
        "head": "feature-branch",
        "base": "main"
    }

    response = requests.post(url, json=data, headers=headers)

    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    return response.json()





















# from dotenv import load_dotenv
# load_dotenv()
# token = os.getenv("GITHUB_TOKEN")