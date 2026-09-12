from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain.tools import tool
from rich import print

model = ChatGroq(model="openai/gpt-oss-20b")


@tool
def get_text_length(text: str) -> int:
    """Returns number of characters in given text."""
    return len(text)


# Tool binding
llm_with_tool = model.bind_tools([get_text_length])

result = llm_with_tool.invoke(
    "Returns number of characters in given text: 'how are you'"
)

if result.tool_calls:
    tool_call = result.tool_calls[0]

    tool_name = tool_call["name"]
    tool_args = tool_call["args"]

    tool_result = get_text_length.invoke(tool_args)

    final_response = llm_with_tool.invoke(
        f"The length of the text is {tool_result}"
    )

    print(final_response)