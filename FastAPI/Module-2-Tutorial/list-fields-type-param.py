from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name : str
    desc : str | None = None
    price : float
    tax : float | None = None
    tags : List[str] = None
    # Basically, The following line is also supported without importing List from typing
    # tags : list[str] = None


@app.put("/items/{item_id}")
async def update_item(item_id : int, item : Item):
    results = {"item_id" : item_id, "item" : item}
    return results
