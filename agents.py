import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def transform_query(query: str) -> str:
    return f"Please explain in detail: {query}"

def generate_response(original: str, transformed: str) -> str:
    try:
        response = model.generate_content(f"Original: {original}\nTransformed: {transformed}")
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

