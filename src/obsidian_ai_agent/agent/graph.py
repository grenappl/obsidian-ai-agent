from langchain.messages import HumanMessage
from langchain_core.messages.base import BaseMessage
from langgraph.graph import END, START, StateGraph
from langgraph.graph.state import CompiledStateGraph

from .nodes import NODES
from .state import AgentState

graph: CompiledStateGraph = None


def _route_user_intent(state: AgentState):
    return state.get("user_intent")


def _route_agent_action(state: AgentState):
    return state.get("agent_action")


def build_graph():
    global graph

    graph_builder = StateGraph(AgentState)
    for node in NODES:
        graph_builder.add_node(node.name, node.func)

    graph_builder.add_edge(START, "classifier")
    graph_builder.add_conditional_edges(
        NODES[0].name,
        _route_user_intent,
        {
            "chat": "chatbot",
            "read": "read_router",
            "make": "generator",
            "edit": "editor",
        },
    )

    graph_builder.add_edge(NODES[1].name, END)

    graph_builder.add_conditional_edges(
        NODES[2].name,
        _route_agent_action,
        {
            "summarize": "summarizer",
            "analyze": "analyst",
            "question": "inquirer",
        },
    )
    graph_builder.add_edge(NODES[3].name, END)
    graph_builder.add_edge(NODES[4].name, END)
    graph_builder.add_edge(NODES[5].name, END)

    graph_builder.add_edge(NODES[6].name, END)
    graph_builder.add_edge(NODES[7].name, END)

    graph = graph_builder.compile()


def view_graph():
    pass


def run_graph(query):
    input = {"messages": [HumanMessage(query)]}
    res = graph.invoke(input)

    print(res)
    for msg in res["messages"]:
        msg: BaseMessage
        msg.pretty_print()
        print()

    print(f"User Intent: {res['user_intent']}")
    print(f"Agent Action: {res['agent_action']}")
    print()
