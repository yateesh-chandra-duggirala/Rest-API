from fastapi import FastAPI, Header
from typing import Annotated, List, Union

app = FastAPI()

@app.get("/items/")
async def get_item(x_token : Annotated[Union[List[str] , None], Header()] = None):
    return {"X-Token" : x_token}