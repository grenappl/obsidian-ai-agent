import os


class IOPaths:
    def __init__(self, file, folder):
        self.file = file
        self.folder = folder


INPUT = IOPaths("PROMPT.md", "Inputs")
OUTPUT = IOPaths("RESPONSE.md", "Outputs")
ENCODING = "utf-8"

MODEL = "gemini-2.5-flash"
PROVIDER = "google-genai"


def get_API_KEY1():
    return os.getenv("GEMINI_API_KEY_1")


def get_API_KEY2():
    return os.getenv("GEMINI_API_KEY_2")


AGENT_ACTIONS = ["chat", "summarize", "analyze", "question", "make", "edit"]
