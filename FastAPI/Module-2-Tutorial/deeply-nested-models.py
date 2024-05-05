from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    img : HttpUrl
    name : str

class Item(BaseModel):
    name : str
    desc : str | None = None
    price : float
    tax : float | None = None
    tags : set[str] = set()
    images : list[Image] | None = None

class Offer(BaseModel) :
    name : str
    desc : str | None = None
    price : float
    items : list[Item] | None = None

@app.post("/offers/")
async def create_offer(offer : Offer):
    return offer