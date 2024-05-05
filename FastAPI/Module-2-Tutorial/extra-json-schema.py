from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name : str
    desc : str | None = None
    price : float
    tax : float | None = None

    class Config:
        schema_extra = {
            "examples" : [
                {
                    "name" : "Python",
                    "desc" : "Python is an interpreted Language",
                    "price" : 35.4,
                    "tax" : 3.2
                }
            ]
        }

@app.put("/items/{item_id}")
async def update_item(item_id : int, item : Item):
    results = {"item_id" : item_id, "item" : item}
    return results