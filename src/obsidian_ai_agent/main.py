from dotenv import load_dotenv

from obsidian_ai_agent.cli.display import get_command
from obsidian_ai_agent.config.settings import INPUT
from obsidian_ai_agent.content.io import create_io, read_file

from .agent import graph


def main():
    load_dotenv()
    create_io()
    graph.build_graph()

    running = True
    while running:
        cmd = input("Obsidian Agent> ").strip().lower()
        cmd_res = get_command(cmd)

        if cmd_res == True:
            prompt = read_file(INPUT.file).strip()
            graph.run_graph(prompt)
        elif cmd_res == False:
            running = False
            break


if __name__ == "__main__":
    main()
