from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain.tools import tool 
from rich import print 
model = ChatGroq(model="openai/gpt-oss-20b")
def get_text_length(text:str)->int:
    """Returns number of character in given text"""
    return len(text)
#tool binding
llm_with_tool=model.bind_tools([get_text_length])

result2=llm_with_tool.invoke("Returns number of character in given text : 'how are you'")

print(result2.tool_calls[0])