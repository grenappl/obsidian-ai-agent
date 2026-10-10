from typing import Literal

from langgraph.graph import MessagesState
from pydantic import BaseModel, Field

UserIntent = Literal["chat", "read", "make", "edit"]
AgentAction = Literal["chat", "summarize", "analyze", "question", "make", "edit"]


class ClassifierResult(BaseModel):
    user_intent: UserIntent = Field(
        description="What the user wants to do with their notes."
    )
    agent_action: AgentAction = Field(
        description="The next action the assistant should take."
    )


class AgentState(MessagesState):
    user_intent: UserIntent
    agent_action: AgentAction
