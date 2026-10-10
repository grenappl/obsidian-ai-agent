from types import FunctionType

from . import llm as LLM
from .state import AgentState


def classify_prompt(state: AgentState):
    print("Classifying prompt...")
    output = LLM.run_classifier(state["messages"][-1].content)
    print(output)
    return {"user_intent": output.user_intent, "agent_action": output.agent_action}


def run_chatbot(state: AgentState):
    print("Running chat model...")
    # output = LLM.run_agent(state.get("agent_action"))
    return {}


def route_reader(state: AgentState):
    print("Routing to reading agent...")
    return {}


def run_summarizer(state: AgentState):
    print("Running summarizer...")
    return {}


def run_analyst(state: AgentState):
    print("Running analyst...")
    return {}


def run_inquirer(state: AgentState):
    print("Running inquirer...")
    return {}


def generate_note(state: AgentState):
    print("Running generator...")
    return {}


def edit_note(state: AgentState):
    print("Running Editor...")
    return {}


# def ask_approval(state: AgentState):
#     print("Asking for approval...")
#     return {}


class GraphNode:
    def __init__(self, name, func):
        self.name: str = name
        self.func: FunctionType = func


NODES: list[GraphNode] = [
    GraphNode("classifier", classify_prompt),
    GraphNode("chatbot", run_chatbot),
    GraphNode("read_router", route_reader),
    GraphNode("summarizer", run_summarizer),
    GraphNode("analyst", run_analyst),
    GraphNode("inquirer", run_inquirer),
    GraphNode("generator", generate_note),
    GraphNode("editor", edit_note),
]
