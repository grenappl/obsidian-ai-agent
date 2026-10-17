from obsidian_ai_agent.config.settings import AGENT_ACTIONS
from obsidian_ai_agent.content.io import write_agent_response

from . import llm as LLM
from .schemas import AgentState


def classifier(state: AgentState):
    output = LLM.run_classifier(state["messages"][-1].content)
    return {"action": output.action}


def chatbot(state: AgentState):
    output = LLM.run_assistant(AGENT_ACTIONS[0], state["messages"][-1].content)
    return {"messages": [output]}


def load_context(state: AgentState):
    print("Loading context...")
    return {}


def summarizer(state: AgentState):
    print("Running summarizer...")
    return {}


def analyst(state: AgentState):
    print("Running analyst...")
    return {}


def inquirer(state: AgentState):
    print("Running inquirer...")
    return {}


def generator(state: AgentState):
    print("Running generator...")
    return {}


def editor(state: AgentState):
    print("Running Editor...")
    return {}


def response(state: AgentState):
    write_agent_response(state["messages"][-1].content)


NODES = [
    classifier,
    chatbot,
    load_context,
    summarizer,
    analyst,
    inquirer,
    generator,
    editor,
    response,
]
