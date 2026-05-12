from pydantic import BaseModel
from typing import Optional
# User model
class User(BaseModel):
    id: int
    username: str
    email: str
# Pet model
class Pet(BaseModel):
    id: int
    name: str
    species: str
    age: Optional[int] = None
    owner_id: int
# Message model
class Message(BaseModel):
    id: int
    username: str
    text: str
    