from fastapi import FastAPI
from pydantic import BaseModel, EmailStr


app = FastAPI()

class BaseUser(BaseModel):
    username : str
    email : EmailStr
    fullname : str | None = None

class UserIn(BaseUser):
    password : str

@app.post("/user/", response_model=BaseUser)
async def add_user(user : BaseUser) -> BaseUser:
    return user