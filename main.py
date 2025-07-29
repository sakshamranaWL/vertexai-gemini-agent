from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from agents import transform_query, generate_response
import os

load_dotenv()
app = FastAPI()

class AskRequest(BaseModel):
    query: str

@app.post("/ask")
async def ask(request: AskRequest):
    query = request.query.strip()
    if not query:
        raise HTTPException(status_code=400, detail="Query cannot be empty.")

    try:
        enhanced = transform_query(query)
        final = generate_response(query, enhanced)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")

    return {
        "original_query": query,
        "enhanced_query": enhanced,
        "final_response": final
    }




