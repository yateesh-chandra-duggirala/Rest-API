from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
async def read_users():
    return ["Yateesh", "Chandra"]

@app.get("/users")
async def read_users_2():
    return ["Real", "User"]