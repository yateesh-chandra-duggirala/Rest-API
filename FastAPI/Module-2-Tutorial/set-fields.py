from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name : str
    desc : str | None = None
    price : float
    tax : float | None = None
    tags : set[str] = set()

@app.put("/items/{item_id}")
async def update_item(item_id : int, item : Item):
    res = {"item_id" : item_id, "item" : item}
    return res