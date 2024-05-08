from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserBase(BaseModel):
    username : str
    email : EmailStr
    fullname : str | None = None

class UserIn(UserBase):
    password : str

class UserOut(UserBase):
    pass

class UserInDB(UserBase):
    hashed_password : str

def fake_password(raw : str):
    return "secret" + raw 

def fake_user_save(user_in : UserIn):
    hashed_ = fake_password(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_)
    return user_in_db

@app.post("/user/", response_model=UserOut)
async def register_user(user_in : UserIn):
    user_save = fake_user_save(user_in)
    return user_save