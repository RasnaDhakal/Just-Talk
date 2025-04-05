import os
from langchain_community.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage
from dotenv import load_dotenv
from langchain.chains import LLMChain

load_dotenv()  # Loads variables from .env

# LangSmith tracing
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2", "false")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT", "llama-english-chatbot")

llm = ChatOllama(model="llama2", temperature=0.7)

# Read prompt from the .txt file
with open(r"C:\Users\User\Desktop\llama-chatbot\backend\app\prompts\chat_prompt.txt", "r") as f:
    prompt_str = f.read()

# Set up LangChain template with user input placeholder
prompt_template = ChatPromptTemplate.from_template(prompt_str)

# Create LangChain chain with LLaMA model and the prompt
chain = LLMChain(prompt=prompt_template, llm=llm)

# Function to get the chatbot response
def get_chatbot_response(user_input):
    return chain.invoke({"user_input": user_input})
