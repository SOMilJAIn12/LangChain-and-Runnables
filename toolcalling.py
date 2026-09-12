from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain.tools import tool
from rich import print
from langchain_core.messages import HumanMessage
model = ChatGroq(model="openai/gpt-oss-20b")


@tool
def get_text_length(text: str) -> int:
    """Returns number of characters in given text."""
    return len(text)


# Tool binding
llm_with_tool = model.bind_tools([get_text_length])

quary=HumanMessage("return the number of character in given text : 'How are you'")
message=[]
message.append(quary)
result=llm_with_tool.invoke(message)
message.append(result)

if result.tool_calls:
    tool_name=result.tool_calls[0]["name"]
    #tool_name.invoke()