from langchain.tools import tool
from logger import log

@tool("create_note", description=(
    """
    Create a note with user desired content. 
    Use any title for the note if not specified by the user. 
    Do not include the title of the note in the content
    """
))
def create_note(text_content: str, note_title: str):
    msg = f"Content is being written in './Outputs/{note_title}'"
    log("System", msg)
    print(msg)
    with open(f"./Outputs/{note_title}.md", "w", encoding="utf-8") as note:
        note.write(text_content)

@tool("read_note", description=(
    "Read the contents of a note in a specific folder or directory"
))
def read_note(note_title: str, directory: str="."):
    msg = f"'{note_title}' note is being read"
    log("System", msg)
    print(msg)
    try:
        with open(f"../{directory}/{note_title}.md", "r+", encoding="utf-8") as note:
            return note.read()
    except FileNotFoundError:
        return "Error: Note does not exist"
    except Exception as e:
        e = str(e)
        return f"Error: {e}"

@tool("append_to_note", description=(
    """
    Appends or creates content to be appended to a note in a specific folder or directory. 
    Use this tool if the user says to create content within a specific note instead of making a new note.
    """
))
def append_to_note(note_title: str, note_content: str, directory: str="."):
    msg = f"Content is being appended to '{directory}/{note_title}'"
    log("System", msg)
    print(msg)
    try:
        with open(f"../{directory}/{note_title}.md", "a", encoding="utf-8") as note:
            note.write(f"\n\n# AI Generated Content\n---\n{note_content}\n---\n")
    except FileNotFoundError:
        return "Error: Note does not exist"
    except Exception as e:
        e = str(e)
        return f"Error: {e}"