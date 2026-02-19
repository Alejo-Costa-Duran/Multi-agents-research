import sys
from main import app

def run():
    # --- DYNAMIC PROMPT LOGIC ---
    # sys.argv[0] is the script name ('run-test.py')
    # sys.argv[1:] takes everything you typed after the filename
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        # Fallback if you forget to type a prompt
        query = "Explain the XY model in 2 sentences."
    
    inputs = {"messages": [("user", query)]}
    
    print(f"--- Sending Query to Agents: {query} ---", flush=True)
    
    for chunk in app.stream(inputs, stream_mode="updates"):
        for node_name, data in chunk.items():
            print(f"\n[NODE FINISHED]: {node_name}", flush=True)
            if "messages" in data:
                print(f"Content: {data['messages'][-1].content}", flush=True)

if __name__ == "__main__":
    run()