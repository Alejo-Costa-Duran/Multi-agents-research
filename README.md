# Multi-Agent Physics Research System

A proof-of-concept multi-agent system for physics research, built with LangGraph and local LLMs via Ollama. Given a natural language query about a physical system, it searches for relevant papers and generates draft Python implementations.

## Architecture

The system uses a two-agent pipeline orchestrated by a LangGraph `StateGraph`:

```
User Query → Researcher → Coder → Output
```

| Agent | Model | Role |
|-------|-------|------|
| **Researcher** | `llama3.1:8b` | Searches the web for relevant papers and extracts key findings using Tavily |
| **Coder** | `deepseek-r1:7b` | Takes the research output and generates Python code to simulate or verify the physics |

The agents are intentionally assigned to different models: `llama3.1` handles tool use and web search, while `deepseek-r1` is used for its stronger reasoning on math and logic tasks.

## Example

```bash
python run-test.py "Find the Hamiltonian for a 2D Ising model and write a Python function to calculate the energy of a 4x4 spin lattice."
```

The researcher fetches relevant results, then the coder produces a working Python implementation based on those findings.

## Getting Started

### Prerequisites

- [Ollama](https://ollama.ai/) running locally with `llama3.1:8b` and `deepseek-r1:7b` pulled
- A [Tavily](https://tavily.com/) API key for web search

### Run locally

```bash
pip install -r requirements.txt
export TAVILY_API_KEY=your_key_here
python run-test.py "Your physics query here"
```

### Run with Docker

```bash
export TAVILY_API_KEY=your_key_here
docker-compose up --build
```

The Docker setup uses `host.docker.internal` to reach the Ollama instance running on the host machine.

## Roadmap

- [ ] Prompt enhancer agent to refine ambiguous queries before search
- [ ] Code reviewer agent to validate and test generated implementations
- [ ] Physics reviewer agent to sanity-check outputs against known results
- [ ] arXiv-specific search tool to complement general web search

## Stack

- [LangGraph](https://github.com/langchain-ai/langgraph) — agent orchestration
- [LangChain](https://github.com/langchain-ai/langchain) — agent and tool abstractions
- [Ollama](https://ollama.ai/) — local LLM inference
- [Tavily](https://tavily.com/) — web search API
- Docker — containerized deployment