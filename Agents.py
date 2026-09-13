from dotenv import load_dotenv
load_dotenv()
import os
import requests
from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain_core.messages import HumanMessage,ToolMessage
from tavily import TavilyClient
## lets create tool

def get_weather(city:str)->str:
    """Get current weather of the city"""
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()