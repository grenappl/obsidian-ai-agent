def run():
    return True


def exit():
    print("Closing agent...")
    return False


def help():
    pass


def prompt(txt: str):
    txt = txt.replace("prompt", "")[1:-1]
    print(txt)


def query(txt: str):
    txt = txt.replace("query", "")[1:-1]


def repo(txt: str):
    txt = txt.replace("repo", "")[1:-1]
