from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def get_react_code_review_chain():
    template = """
You are an expert React, JavaScript, and Next.js code reviewer.

Please review the following code and provide:
- Code quality issues
- Performance problems
- React/Next.js anti-patterns
- Accessibility violations
- Suggestions for improvement

Code:
```jsx
{code}
Your review:"""
    prompt = PromptTemplate(
    input_variables=["code"],
    template=template,
    )
    llm = ChatOpenAI(temperature=0.2, model="gpt-4")
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain