from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from agents import transform_query, generate_response
import os
import traceback

load_dotenv()
app = FastAPI()

class AskRequest(BaseModel):
    query: str

@app.post("/ask")
async def ask(request: AskRequest):
    query = request.query
    try:
        print(f"Received query: {query}")
        enhanced = transform_query(query)
        print(f"Enhanced query: {enhanced}")
        final = generate_response(query, enhanced)
        print(f"Final response: {final}")

        return {
            "original_query": query,
            "enhanced_query": enhanced,
            "final_response": final
        }
    except Exception as e:
        print("❌ ERROR in /ask endpoint:")
        traceback.print_exc()
        return {"error": str(e)}


