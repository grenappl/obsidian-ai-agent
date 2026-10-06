from dotenv import load_dotenv
from langchain.messages import AIMessage, HumanMessage

from .agent.workflow import Workflow


def main():
    load_dotenv()

    workflow = Workflow()
    workflow.create_io()
    res: dict[str, AIMessage] = workflow.start({"messages": [HumanMessage("hi!")]})

    print(res["messages"][1].content)


if __name__ == "__main__":
    main()
