from fastapi import FastAPI
from models import User, Pet, Message
app = FastAPI()
@app.get("/health")
def health():
    return {"status": "ok"}
from pydantic import BaseModel
class UserRegister(BaseModel):
    username: str
    email: str
    password: str
class UserLogin(BaseModel):
    username: str
    password: str
users_db = []  # MVP: säilytetään käyttäjät muistissa
@app.post("/register")
def register(user: UserRegister):
    # tarkista, onko käyttäjä jo olemassa
    for u in users_db:
        if u["username"] == user.username:
            return {"status": "error", "message": "User already exists"}
    users_db.append(user.dict())
    return {"status": "registered"}
@app.post("/login")
def login(user: UserLogin):
    for u in users_db:
        if u["username"] == user.username and u["password"] == user.password:
            return {"status": "success"}
    return {"status": "error", "message": "Invalid credentials"}