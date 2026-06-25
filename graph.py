from langgraph.graph import StateGraph,START,END
from typing import Annotated,TypedDict


class State(TypedDict):
    code : str
    language: str
    code_review : str

def graph(state: State) -> State:
    
    graph_builder = StateGraph()
    
    graph_builder.add_edge(START,END)