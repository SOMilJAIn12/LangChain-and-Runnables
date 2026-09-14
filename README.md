# LangChain-and-Runnables

A hands-on repository for learning and experimenting with **LangChain, Runnables, Tool Calling, Agents, and LLM-based workflows**.

This repository contains small, focused examples that demonstrate different LangChain concepts through practical Python programs.

## 📚 Topics Covered

- LangChain Runnables
- RunnableSequence
- RunnablePassthrough
- RunnableParallel
- Tool Calling
- Custom Tools
- Agents
- LLM Integration
- Environment Variables
- AI-powered workflows

## 🛠️ Tech Stack

- Python
- LangChain
- LangGraph
- Groq
- OpenAI-compatible LLMs
- python-dotenv

## 📂 Project Structure

```text
LangChain-and-Runnables/
│
├── Agents.py
├── newssummarizer.py
├── owntool.py
├── parallelrunnable.py
├── runnablePassthrough.py
├── sequencerrunnable.py
├── toolcalling.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/SOMilJain12/LangChain-and-Runnables.git
cd LangChain-and-Runnables
```

### Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the root directory and add your API key:

```env
GROQ_API_KEY=your_groq_api_key
```

Load the variables in Python:

```python
from dotenv import load_dotenv

load_dotenv()
```

> **Note:** Never commit your `.env` file or expose your API keys publicly.

## 🔗 Runnables

LangChain Runnables provide a standard interface for building and composing LLM workflows.

Common Runnable methods include:

```python
.invoke()
.batch()
.stream()
```

### RunnableSequence

`RunnableSequence` executes multiple steps sequentially. The output of one step becomes the input of the next.

```python
chain = prompt | model | parser

result = chain.invoke(input)
```

The `|` operator makes it easy to compose multiple Runnables into a single pipeline.

### RunnablePassthrough

`RunnablePassthrough` allows the original input to pass through a workflow without modification.

```python
from langchain_core.runnables import RunnablePassthrough

chain = {
    "context": retriever,
    "question": RunnablePassthrough()
}
```

### RunnableParallel

`RunnableParallel` runs multiple Runnables independently using the same input.

```python
from langchain_core.runnables import RunnableParallel

chain = RunnableParallel(
    first=chain_1,
    second=chain_2
)

result = chain.invoke(input)
```

The result contains the output from each Runnable.

## 🛠️ Custom Tools

LangChain can convert Python functions into tools that an LLM can use.

```python
from langchain.tools import tool

@tool
def get_text_length(text: str) -> int:
    """Returns the number of characters in the given text."""
    return len(text)
```

The tool can then be bound to a model:

```python
model_with_tools = model.bind_tools([get_text_length])
```

## 🔧 Tool Calling

Tool calling allows an LLM to interact with functions instead of only generating text.

A typical workflow is:

```text
User Input
    ↓
LLM
    ↓
Tool Selection
    ↓
Tool Execution
    ↓
Tool Result
    ↓
LLM Response
```

This is useful for applications that need calculations, external data, APIs, or custom Python functions.

## 🤖 Agents

Agents allow an LLM to dynamically decide which actions or tools are required to complete a task.

A basic agent can be created using LangChain:

```python
from langchain.agents import create_agent

agent = create_agent(
    model=model,
    tools=[get_text_length]
)
```

The agent can then be invoked with a message:

```python
result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "How many characters are in LangChain?"
        }
    ]
})
```

Agents can:

- Understand the user's request
- Decide which tool to use
- Execute the selected tool
- Process the tool result
- Generate a final response

## 📰 News Summarizer

`newssummarizer.py` contains an LLM-powered workflow for processing and summarizing news content.

Run it with:

```bash
python newssummarizer.py
```

## ▶️ Running the Examples

Each Python file demonstrates a different LangChain concept.

```bash
python sequencerrunnable.py
python runnablePassthrough.py
python parallelrunnable.py
python toolcalling.py
python owntool.py
python Agents.py
python newssummarizer.py
```

Make sure the required API keys are configured in `.env` before running the examples.

## 🎯 Purpose

This repository is a learning and experimentation project focused on understanding how LangChain's Runnable architecture, tool calling, and agents can be used to build modern LLM applications.

The examples are intentionally small so that individual concepts can be understood before combining them into larger AI workflows.

## 📌 Future Improvements

- Add more Runnable examples
- Explore structured outputs
- Add more tool-calling examples
- Explore agent workflows in greater depth
- Build more practical LLM applications
- Experiment further with LangGraph
- Add RAG-based workflows

## 👨‍💻 Author

**Somil Jain**

GitHub: https://github.com/SOMilJain12

---

⭐ If you find this repository useful, consider giving it a star!
