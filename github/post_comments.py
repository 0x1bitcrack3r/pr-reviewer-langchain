# github/post_comments.py
from github import Github
import os
from dotenv import load_dotenv

load_dotenv()
g = Github(os.getenv("GITHUB_TOKEN"))

def upsert_summary_comment(pr, new_body, tag="<!--ai-reviewer-->"):
    comments = pr.get_issue_comments()
    for c in comments:
        if tag in c.body:
            c.edit(f"{tag}\n{new_body}")
            return
    pr.create_issue_comment(f"{tag}\n{new_body}")

def post_inline_comments(pr_url, comments):
    owner, repo_name, pr_number = parse_pr_url(pr_url)
    repo = g.get_repo(f"{owner}/{repo_name}")
    pr = repo.get_pull(int(pr_number))
    commit = pr.get_commits().reversed[0]

    for comment in comments:
        pr.create_review_comment(
            body=comment["body"],
            commit_id=commit.sha,
            path=comment["file"],
            line=comment["line"],
            side="RIGHT"
        )

def post_summary_comment(pr_url, summary_text):
    owner, repo, pr_number = parse_pr_url(pr_url)
    repo = g.get_repo(f"{owner}/{repo}")
    pr = repo.get_pull(int(pr_number))
    upsert_summary_comment(pr, summary_text)

def parse_pr_url(pr_url):
    parts = pr_url.strip().split("/")
    return parts[3], parts[4], parts[-1]

def compute_risk_score(num_lines, critical_files, num_lint_issues, ai_flags):
    score = 0
    if num_lines > 500: score += 3
    elif num_lines > 100: score += 2
    elif num_lines > 50: score += 1
    score += len([f for f in critical_files if "auth" in f or "payment" in f]) * 2
    score += min(num_lint_issues // 5, 3)
    score += min(ai_flags, 3)
    return min(score, 10)
