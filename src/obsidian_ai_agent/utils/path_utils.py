from pathlib import Path

IO = {"folders": ["Inputs", "Outputs"], "files": ["PROMPT.md", "RESPONSE.md"]}


def create_io():
    for folder in IO["folders"]:
        dirpath = Path(folder)
        create_dir(dirpath)

    for file in IO["files"]:
        filepath = Path(file)
        create_file(filepath)


def create_dir(dirpath):
    if not dirpath.exists():
        dirpath.mkdir()


def create_file(filepath):
    if not filepath.exists():
        with open(filepath, "x") as f:
            f.write("")


def read_file(filepath):
    with open(filepath, "r") as f:
        return f.read()
