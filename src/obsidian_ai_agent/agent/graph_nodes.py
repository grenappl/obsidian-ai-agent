from langchain.messages import AIMessage
from langgraph.graph import MessagesState


def node1(state: MessagesState):
    return {"messages": [AIMessage("hello world")]}


def node2():
    pass


def node3():
    pass
