from langchain_core.messages.base import BaseMessage

from .commands import exit, help, prompt, query, repo, run


def get_command(cmd: str) -> bool:
    if cmd in ["exit", "e"]:
        return exit()
    if cmd == "run":
        return run()
    elif cmd == "help":
        return help()
    elif "prompt" in cmd:
        return prompt(cmd.replace("prompt", "").strip())
    elif "query" in cmd:
        return query(cmd.replace("query", "").strip())
    elif "repo" in cmd:
        return repo(cmd.replace("repo", "").strip())


def print_workflow_messages(res):
    print()
    for msg in res["messages"]:
        msg: BaseMessage
        msg.pretty_print()
        print()
    print(f"\nAction: {res['agent_action']}\n")
