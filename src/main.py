from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openrouter import ChatOpenRouter
from langchain.agents import create_agent
from dotenv import load_dotenv

from agents import MODEL, TOOLS, get_sys_prompt
from logger import log

load_dotenv()

LLM = ChatGoogleGenerativeAI(model=MODEL)
# LLM = ChatOpenRouter(model=MODEL)

agent = create_agent(
    model=LLM,
    tools=TOOLS
)

def get_user_prompt() -> str:
    with open("Input.md", "r", encoding="utf-8") as prompt_content:
        return prompt_content.read()
    
def run_agent(user_prompt: str, action: str) -> str:
    sys_prompt = get_sys_prompt(action)
    res = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": user_prompt
            },
            {
                "role": "system",
                "content": sys_prompt
            }
        ]
    })
    content = res["messages"][-1].content
    if isinstance(content, list):
        content = "".join(part["text"] for part in content if part.get("type") == "text")
    print("\n" + content + "\n")
    return content

def main():
    running: bool = True

    while running:
        response: str

        print("- /inform")
        print("- /summarize")
        print("- /create")
        print("- /test")
        print("- /exit")
        print()
        print("> ", end="")
        cmd: str = input()
        print()

        if cmd != "/exit":
            try:
                user_prompt = get_user_prompt()
                log("User", user_prompt)
                response = run_agent(user_prompt, cmd)
            except Exception as e:
                str_e = str(e)
                if str_e == "[Errno 11001] getaddrinfo failed":
                    response = "Not connected to the internet!"
                else:
                    response = f"ERROR: {str_e}"
                print("Something went wrong!")

            with open("Response.md", "w", encoding="utf-8") as response_file:
                response_file.write(response)
                log("Agent", response)
            print()
        else:
            running = False

if __name__ == "__main__":
    main()