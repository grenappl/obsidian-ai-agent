from typing import TypedDict


class AgentState(TypedDict):
    messages: list
    intent: str | None
    note_id: str | None
    search_results: list
    response: str | None
