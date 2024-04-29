from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name : str
    desc : str | None = None
    price : float
    tax : float | None = None

@app.post("/items/")
async def create_item(item : Item):
    if item.tax is None :
        item.tax = item.price * 0.025
    return item

@app.put("/items/{item_id}")
async def update_item(item_id : int, item : Item):
    return {"item_id" : item_id, **item.dict()}