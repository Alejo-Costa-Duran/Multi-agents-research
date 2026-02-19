from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, List
import operator

class AgentState(TypedDict):
    messages: Annotated[List, operator.add]
    next_agent: str

def supervisor(state):
    if not state.get("next_agent"):
        return {"next_agent": "researcher"}
    elif state["next_agent"] == "researcher":
        return {"next_agent": "coder"}
    else:
        return {"next_agent": END}

workflow = StateGraph(AgentState)
workflow.add_node("researcher", researcher)
workflow.add_node("coder", coder)

workflow.set_entry_point("researcher")
workflow.add_edge("researcher", "coder")
workflow.add_edge("coder", END)

app = workflow.compile()