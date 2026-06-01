from tools import note, pdf

MODEL = "gemini-2.5-flash"
# MODEL = "nvidia/nemotron-3-super-120b-a12b:free"

TOOLS = [
    note.create_note,
    note.read_note,
    note.append_to_note,

    pdf.read_pdf
]

def get_sys_prompt(action: str):
    print(f"action: {action}")
    match action:
        case "/inform":
            with open("./Prompts/Informer.md", "r") as note:
                prompt = note.read()
        case "/summary":
            with open("./Prompts/Summarizer.md", "r") as note:
                prompt = note.read()
        case "/create":
            with open("./Prompts/Creator.md", "r") as note:
                prompt = note.read()
        case "/test":
            with open("./Prompts/Tester.md", "r") as note:
                prompt = note.read()
        case _:
            raise Exception("Invalid cmd prompt!")
    return prompt