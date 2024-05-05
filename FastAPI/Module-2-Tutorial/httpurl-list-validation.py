from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from typing import List

app = FastAPI()

class Image(BaseModel):
    url : HttpUrl
    name : str

class Item(BaseModel):
    name : str
    desc : str | None = None
    price : float
    tax : float | None = None
    image : List[Image]

@app.put("/items/{item_id}")
async def update_item(item_id : int, item : Item):
    res = {"item_id" : item_id, "item" : item}
    return res