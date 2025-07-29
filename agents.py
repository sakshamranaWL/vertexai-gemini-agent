# agents.py

import os
from langchain_google_vertexai import ChatVertexAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

project_id = os.getenv("PROJECT_ID")
region = os.getenv("REGION", "global")

# Load models
llm_1 = ChatVertexAI(model="gemini-1.5-flash", project=os.getenv("PROJECT_ID"), location=os.getenv("REGION","global"))
llm_2 = ChatVertexAI(model="gemini-1.5-flash", project=os.getenv("PROJECT_ID"), location=os.getenv("REGION","global"))

# Prompt 1: Transform
prompt_1 = PromptTemplate.from_template(
    "Rewrite or enhance the following query with more relevant context:\nQuery: {query}\nRewritten:"
)

# Prompt 2: Final response
prompt_2 = PromptTemplate.from_template(
    "Original: {original}\nEnhanced: {enhanced}\nFinal Answer:"
)

def transform_query(user_query: str) -> str:
    return llm_1.invoke(prompt_1.format(query=user_query)).content

def generate_response(original: str, enhanced: str) -> str:
    return llm_2.invoke(prompt_2.format(original=original, enhanced=enhanced)).content
