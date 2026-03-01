from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from dotenv import load_dotenv

from agent import MODEL, SYS_PROMPT, TOOLS
from logger import log

load_dotenv()

LLM = ChatGoogleGenerativeAI(model=MODEL)
agent = create_agent(
    model=LLM,
    system_prompt=SYS_PROMPT,
    tools=TOOLS
)

def get_user_prompt() -> str:
    with open("Prompt.md", "r+") as prompt_content:
        return prompt_content.read()
    
def run_agent(user_prompt: str) -> str:
    res = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    })
    content = res["messages"][-1].content
    if isinstance(content, list):
        content = "".join(part["text"] for part in content if part.get("type") == "text")
    return content

def main():
    response = ""
    try:
        user_prompt = get_user_prompt()
        log("User", user_prompt)
        response = run_agent(user_prompt)
    except Exception as e:
        str_e = str(e)
        response = f"ERROR: {str_e}"
        print("Something went wrong!")

    with open("Response.md", "w") as response_file:
        response_file.write(response)
    log("Agent", response)

if __name__ == "__main__":
    main()