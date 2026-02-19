from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, List
import operator
from agents import researcher, coder
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

if __name__ == "__main__":
    # Your test query
    inputs = {"messages": [("user", "Find the Hamiltonian for a 2D Ising model and write a Python function to calculate the energy of a 4x4 spin lattice.")]}
    
    # Run the graph and stream the output
    for output in app.stream(inputs):
        for key, value in output.items():
            print(f"\n--- Node: {key} ---")
            # Print the latest message content from that node
            if "messages" in value:
                print(value["messages"][-1].content)