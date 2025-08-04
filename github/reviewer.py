from chains.react_code_review import get_react_code_review_chain
from github.client import get_pr_files
from github.post_comments import post_summary_comment, post_inline_comments, compute_risk_score
from utils.diff_parser import extract_line_number

def review_pull_request(pr_url):
    files = get_pr_files(pr_url)
    review_chain = get_react_code_review_chain()

    comments = []
    summary_sections = []
    all_files = []
    total_lines = 0
    ai_flags = 0

    for file in files:
        if not file["filename"].endswith((".js", ".jsx", ".ts", ".tsx")):
            continue

        patch = file.get("patch", "")
        lines = patch.count("\n")
        total_lines += lines
        all_files.append(file["filename"])

        review = review_chain.run(code=patch)
        ai_flags += review.count("⚠️") + review.count("❗") + review.count("❌")

        comments.append({
            "file": file["filename"],
            "line": extract_line_number(patch),
            "body": review.strip()
        })

        summary_sections.append(f"### `{file['filename']}`\n{review.strip()}\n")

    risk_score = compute_risk_score(total_lines, all_files, 0, ai_flags)

    summary = "\n\n".join(summary_sections)
    summary += f"\n\n---\n\n🧮 **PR Risk Score**: `{risk_score}/10`"
    
    post_inline_comments(pr_url, comments)
    post_summary_comment(pr_url, summary)
