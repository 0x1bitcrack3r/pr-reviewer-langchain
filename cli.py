import argparse
from github.reviewer import review_pull_request

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Code Review CLI")
    parser.add_argument("--pr", type=str, required=True, help="GitHub PR URL")
    args = parser.parse_args()

    comments = review_pull_request(args.pr)
    print("\n📋 Review Results:\n")
    for c in comments:
        print(f"- [{c['file']}] {c['review'][:200]}")
        
