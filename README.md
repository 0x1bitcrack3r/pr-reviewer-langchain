# 🤖 LangChain AI Code Reviewer for GitHub PRs

A GitHub-integrated AI code reviewer powered by **LangChain**, **OpenAI GPT-4**, and custom rule logic for **React**, **Next.js**, and **JavaScript**.

It:

- Automatically reviews code on Pull Requests
- Posts inline and summary comments on GitHub
- Assigns a **PR Risk Score** (0-10)
- Can run from CLI, CI, or as an API service

---

## ✨ Features

- ✅ Auto-analyzes changed files on PRs
- 🧠 GPT-4 / LangChain based AI feedback
- 💬 Auto-posts summary and inline comments to GitHub
- 📊 PR Risk Scoring based on code size, critical files, and violations
- ⚙️ CLI tool to run reviews locally or in CI
- 🔌 FastAPI backend (optional) for webhook or REST-based triggers

---

## 🚀 Installation

```bash
git clone https://github.com/your-org/pr-reviewer-langchain.git
cd pr-reviewer-langchain
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🔐 Environment Variables (.env)
```bash
OPENAI*API_KEY=sk-...
GITHUB_TOKEN=ghp*...
```

## 🔧 Run via CLI

```bash
python cli.py --pr https://github.com/owner/repo/pull/42
```

## 🌐 Run via API (FastAPI)

```bash
uvicorn app:app --reload
```

```http
POST /review
{
  "pr_url": "https://github.com/owner/repo/pull/42"
}
```

## 💬 Example PR Comment

### `components/Button.jsx`

- ✅ Good use of memoization.
- ❗ Avoid inline styles in JSX. Consider CSS Modules or styled-components.
- ⚠️ Prop drilling detected, consider Context API.
- 🧮 **PR Risk Score**: `7/10` (High Risk)
