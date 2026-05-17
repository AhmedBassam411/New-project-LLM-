from fastapi import FastAPI
from pydantic import BaseModel
from llm import generate_response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"message": "Backend Running"}

@app.post("/generate")
def generate(request: PromptRequest):

    try:
        response = generate_response(request.prompt)
        return {"response": response}

    except Exception as e:
        return {"response": f"Error: {str(e)}"}