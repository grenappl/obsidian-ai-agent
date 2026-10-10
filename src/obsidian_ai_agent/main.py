from dotenv import load_dotenv

from .agent import graph
from .utils.path_utils import IO, create_io, read_file


def main():
    running = True

    load_dotenv()
    create_io()
    graph.build_graph()

    while running:
        cmd = input("> ").strip().lower()

        if cmd == "q":
            running = False
            break

        prompt = read_file(IO["files"][0]).strip()
        graph.run_graph(prompt)


if __name__ == "__main__":
    main()
