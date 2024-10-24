from src.message import HumanMessage,SystemMessage
from src.inference.gemini import ChatGemini
from src.inference.mistral import ChatMistral
from src.inference.groq import ChatGroq
from src.llm_switcher import LLMSwitcher
from dotenv import load_dotenv
import os

load_dotenv()



llms=[
    ChatGroq(model='llama-3.1-70b-versatile',api_key=os.getenv('GROQ_API_KEY')),
    ChatGemini(model='gemini-1.5-pro',api_key=os.getenv('GOOGLE_API_KEY')),
    ChatMistral(model='open-codestral-mamba',api_key=os.getenv('MISTRAL_API_KEY'))
]

llm_switcher = LLMSwitcher(llms=llms,max_retries=2)
llm_response=llm_switcher.invoke(messages=[SystemMessage('Helpful AI assistant'),HumanMessage('How are you?')])
print(llm_response.content)
