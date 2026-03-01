from langchain.tools import tool
from logger import log

@tool("write_note", description=(
    """
    Create or write to a note in a specific folder or directory.
    Use any title or Outputs directory if neither are specified by the user.
    Do not include the title of the note in the content.
    """
))
def write_note(text_content: str, note_title: str, directory: str="./Outputs"):
    log("System", f"Content is being written in '{directory}/{note_title}'")
    if directory == "./Outputs":
        with open(f"{directory}/{note_title}.md", "w") as note:
            note.write(text_content)
    else:
        with open(f"../{directory}/{note_title}.md", "w") as note:
            note.write(text_content)

@tool("read_note", description=(
    "Read the contents of a note in a specific folder or directory"))
def read_note(note_title: str, directory: str="."):
    log("System", f"'{note_title}' note is being read")
    try:
        with open(f"../{directory}/{note_title}.md", "r+") as note:
            return note.read()
    except FileNotFoundError:
        return "Error: Note does not exist"
    except Exception as e:
        return "Error: Note can not be read"

# @tool("append_to_note", )
def append_to_note(note_title: str, directory: str="."):
    print(f"Content is being appended to '{directory}/{note_title}'")