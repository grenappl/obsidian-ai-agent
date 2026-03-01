import tools.note as nt

MODEL = "gemini-2.5-flash"
SYS_PROMPT = "You are a helpful Obsidian notes assistant. Be concise and accurate with your responses and generation."
TOOLS = [
    nt.write_note,
    nt.read_note
]