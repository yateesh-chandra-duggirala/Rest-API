from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

class BaseItem(BaseModel):
    desc : str
    type : str

class CarItem(BaseItem):
    type : str = "Car"

class PlaneItem(BaseItem):
    type : str = "Plane"
    size : int

items = {
    "item1" : {
        "desc" : "All my friends are Car riders",
        "type" : "car"
    },

    "item2" : {
        "desc": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5
    }
}

# @app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
@app.get("/items/{item_id}", response_model= PlaneItem | CarItem)
async def read_item(item_id : str):
    return items[item_id]