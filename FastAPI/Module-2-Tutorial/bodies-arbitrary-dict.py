from fastapi import FastAPI
from typing import Dict

app = FastAPI()

@app.post("/item-weight/")
async def create_item_weight(weight : Dict[int, str]):
    return weight