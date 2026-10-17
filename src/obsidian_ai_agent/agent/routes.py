# routing.py
from typing import Literal

from obsidian_ai_agent.config.settings import AGENT_ACTIONS

from .schemas import AgentState


def route_classifier(state: AgentState) -> Literal["chatbot", "load_context"]:
    return (
        "load_context"
        if state.get("action") in set(AGENT_ACTIONS) - {AGENT_ACTIONS[0]}
        else "chatbot"
    )


def route_load_context(
    state: AgentState,
) -> Literal["summarizer", "analyst", "inquirer", "generator", "editor"]:
    return {
        "summarize": "summarizer",
        "analyze": "analyst",
        "question": "inquirer",
        "make": "generator",
        "edit": "editor",
    }[state["agent_action"]]
