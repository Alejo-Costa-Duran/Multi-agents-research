from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults

llm = ChatOllama(model="deepseek-r1:14b", base_url="http://localhost:11434")

search_tool = TavilySearchResults(max_results=3)

researcher = create_react_agent(llm, tools=[search_tool], name="researcher")
coder = create_react_agent(llm, tools=[], name="coder")