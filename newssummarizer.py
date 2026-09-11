from dotenv import load_dotenv
load_dotenv()
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
search_tool=TavilySearchResults(max_result=5)
model = ChatGroq(model="openai/gpt-oss-20b")
prompt = ChatPromptTemplate.from_template(
    '''
Yor are a helpful ai assistent
summarize the following news into clear bullet points
{news}
'''
)
chain= prompt | model |StrOutputParser()
news_result= search_tool.run("latest news of 2026")
news=chain.invoke({"news": news_result})
print(news)

print(search_tool.name)
print(search_tool.description)
print(search_tool.args)