from langchain.messages import HumanMessage
from langgraph.graph import END, START, StateGraph
from langgraph.graph.state import CompiledStateGraph

from obsidian_ai_agent.cli.display import print_workflow_messages

from .nodes import NODES
from .routes import route_classifier, route_load_context
from .schemas import AgentState

graph: CompiledStateGraph = None


def build_graph():
    global graph

    g = StateGraph(AgentState)
    # llm_retry = RetryPolicy(max_attempts=3)

    for node in NODES:
        g.add_node(node)  # llm_retry can be applied to retry_policy arg

    g.add_edge(START, "classifier")
    g.add_conditional_edges("classifier", route_classifier)

    g.add_edge("chatbot", "response")

    g.add_conditional_edges("load_context", route_load_context)
    g.add_edge("summarizer", "response")
    g.add_edge("analyst", "response")
    g.add_edge("inquirer", "response")
    g.add_edge("generator", "response")
    g.add_edge("editor", "response")

    g.add_edge("response", END)
    graph = g.compile()


def run_graph(query):
    input = {"messages": [HumanMessage(query)]}
    res = graph.invoke(input)
    print(res["messages"])
    print_workflow_messages(res)
