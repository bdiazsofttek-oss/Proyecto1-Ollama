from fastapi import FastAPI
from pydantic import BaseModel
from ollama import chat

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/ask")
def ask_llama(request: PromptRequest):
    response = chat(
        model="llama3.2:3b",
        messages=[
            {"role": "system", "content": "Eres un asistente útil. Responde en español"},
            {"role": "user", "content": request.prompt},
        ],
    )
    return {"response": response.message.content}
