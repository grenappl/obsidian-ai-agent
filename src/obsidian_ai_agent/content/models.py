from pydantic import BaseModel


class ObsidianNote(BaseModel):
    title: str
    content: str
