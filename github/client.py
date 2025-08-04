import requests
from dotenv import load_dotenv
import os
load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")

def get_pr_files(pr_url):
    # Extract repo info
    parts = pr_url.split("/")
    owner, repo, pr_number = parts[3], parts[4], parts[-1]

    api_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    resp = requests.get(api_url, headers=headers)
    resp.raise_for_status()
    return resp.json()
