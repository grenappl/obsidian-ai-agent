from typing import Literal

from langgraph.graph import MessagesState
from pydantic import BaseModel, Field


class TargetPath:
    def __init__(self, dir: str, files: list[str]):
        self.dir: str = dir
        self.files: list[str] = files


AgentAction = Literal["chat", "summarize", "analyze", "question", "make", "edit"]
AgentStatus = Literal["success", "partial", "error"]


class ClassifierResult(BaseModel):
    action: AgentAction = Field(description="The action the ai assistant should take.")
    target_dir: str = Field(description="Target directory to be looked into")
    target_files: list[str] = Field(
        description="Target file path/s to be viewed inside of target directory"
    )


class AgentState(MessagesState):
    action: AgentAction
    target_path: TargetPath | None = None
    status: AgentStatus | None
