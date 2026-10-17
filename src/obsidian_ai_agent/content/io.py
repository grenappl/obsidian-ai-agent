from pathlib import Path

from obsidian_ai_agent.config.settings import ENCODING, INPUT, OUTPUT


def create_io():
    create_file(INPUT.file)
    create_file(OUTPUT.file)
    create_dir(INPUT.folder)
    create_dir(OUTPUT.folder)


def create_dir(dirpath):
    path = Path(dirpath)
    if not path.exists():
        path.mkdir()


def create_file(filepath, data=""):
    path = Path(filepath)
    if not path.exists():
        path.write_text(data=data, encoding=ENCODING)


def read_file(filepath):
    path = Path(filepath)
    if not path.exists():
        path.read_text(encoding=ENCODING)


def write_agent_response(content: str):
    with open(OUTPUT.file, "w", encoding=ENCODING) as response:
        response.write(content)
