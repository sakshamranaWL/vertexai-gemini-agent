# main.py

from fastapi import FastAPI, Request
from dotenv import load_dotenv
from agents import transform_query, generate_response
import os

load_dotenv()
app = FastAPI()

@app.post("/ask")
async def ask(request: Request):
    body = await request.json()
    query = body.get("query", "")

    enhanced = transform_query(query)
    final = generate_response(query, enhanced)

    return {
        "original_query": query,
        "enhanced_query": enhanced,
        "final_response": final
    }
