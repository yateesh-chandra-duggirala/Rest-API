from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union, List, Any

app = FastAPI()

class Item(BaseModel):
    name : str
    desc : str | None = None
    price : float
    tax : Union[str, None] = None
    tags : List[str] = []

@app.post("/items/", response_model=Item)
async def add_item(item : Item) -> Any:
    return item

@app.get("/items/", response_model=List[Item])
async def read_items() -> any:
    return [
        {"name" : "Python" , "price" : 90.3},
        {"name" : "FastAPI Course", "price" : 43.9},
    ]