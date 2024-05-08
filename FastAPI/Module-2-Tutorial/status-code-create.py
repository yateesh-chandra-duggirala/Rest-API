from fastapi import FastAPI, status

app = FastAPI()

@app.post("/user/", status_code= status.HTTP_201_CREATED)
async def create_user(name : str):
    return {"name" : name}