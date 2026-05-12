from fastapi import FastAPI
from models import User, Pet, Message
app = FastAPI()
@app.get("/health")
def health():
    return {"status": "ok"}
