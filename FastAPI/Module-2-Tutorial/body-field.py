from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Annotated, Union

app = FastAPI()

class Item(BaseModel) : 
    name : str
    desc : Union[str, None] = Field(
        default=None, title="The Description of the item", max_length=10
    )
    price : float = Field(gt=0, description="The price must be greater than zero")
    tax : Union[float, None] = None

@app.put("/items/{item_id}")
async def update_item(item_id : int, item : Annotated[Item, Body(embed=True)]):
    results = {"item_id" : item_id, "item" : item}
    return results