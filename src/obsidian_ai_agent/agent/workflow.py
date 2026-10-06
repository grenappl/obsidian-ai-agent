from pathlib import Path
from typing import Any

from langgraph.graph import END, START, MessagesState, StateGraph

from .graph_nodes import node1

IO = {"folders": ["Inputs", "Outputs"], "files": ["PROMPT.md", "RESPONSE.md"]}


class Workflow:
    def __init__(self):
        self.graph = self.__build_graph()
        # self.llm =

    def __build_graph(self):
        graph = StateGraph(MessagesState)
        for node in [node1]:
            graph.add_node(node)
        for n1, n2 in [
            (START, "node1"),
            ("node1", END),
        ]:
            graph.add_edge(n1, n2)
        return graph.compile()

    def create_io(self) -> None:
        for folder in IO["folders"]:
            dirpath = Path(folder)
            if not dirpath.exists():
                dirpath.mkdir()

        for file in IO["files"]:
            filepath = Path(file)
            if not filepath.exists():
                with open(file, "x") as f:
                    f.write("")

    def start(self, query) -> dict[str, Any]:
        return self.graph.invoke(query)
