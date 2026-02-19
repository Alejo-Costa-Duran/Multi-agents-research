from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults

import os
from langchain_ollama import ChatOllama

# This ensures it uses 'host.docker.internal' when inside Docker
base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

llm = ChatOllama(
    model="deepseek-r1:7b", 
    base_url=base_url,
    temperature=0
)

search_tool = TavilySearchResults(max_results=3)
# researcher = create_react_agent(llm, tools=[search_tool], name="researcher")
# Use a tool-capable model for the researcher:
researcher_llm = ChatOllama(model="llama3.1:8b", base_url=base_url, temperature=0)
researcher = create_react_agent(researcher_llm, tools=[search_tool], name="researcher")

# Keep DeepSeek for the Coder (Logic/Math)
coder = create_react_agent(llm, tools=[], name="coder")