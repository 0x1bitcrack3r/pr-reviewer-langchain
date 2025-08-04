from fastapi import FastAPI, Request
from github.reviewer import review_pull_request

app = FastAPI()

@app.post("/review")
async def review(request: Request):
    body = await request.json()
    pr_url = body.get("pr_url")

    comments = review_pull_request(pr_url)
    return {"comments": comments}
