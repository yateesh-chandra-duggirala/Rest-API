from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Union

app = FastAPI()

class UserIn(BaseModel):
    username : str
    password : str
    email : EmailStr
    fullname : Union[str, None] = None

@app.post("/user/")
async def create_user(user : UserIn) -> UserIn:
    return user