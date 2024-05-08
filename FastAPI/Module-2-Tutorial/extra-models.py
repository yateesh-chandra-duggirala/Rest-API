from fastapi import FastAPI

from pydantic import BaseModel, EmailStr

app = FastAPI()

# Used to pass as input
class UserIn(BaseModel):
    username : str
    password : str
    email : EmailStr
    fullname : str | None = None

# Used to retrieve the output
class UserOut(BaseModel):
    username : str
    email : EmailStr
    fullname : str | None = None

# Used to save the data to database passed through input
class UserInDB(BaseModel) :
    username : str
    hashed_password : str
    email : EmailStr
    fullname : str | None = None

def fake_password_hasher(raw : str):
    # Step - 3 : return the secret password to the fake_save_user method
    return "secret" +  raw

def fake_save_user(user_in : UserIn):

    # Step - 2 : call the function fake_password_hasher from here
    hashed_= fake_password_hasher(user_in.password)

    # Step - 4 : Store the values into the UserInDB class
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password = hashed_)
    return user_in_db

@app.post("/user/",status_code=201, response_model = UserOut)
async def create_user(user_in : UserIn):

    # Step - 1 : call the function fake_save_user from here
    user_saved = fake_save_user(user_in)

    # Step - 5 : return the saved_user
    return user_saved