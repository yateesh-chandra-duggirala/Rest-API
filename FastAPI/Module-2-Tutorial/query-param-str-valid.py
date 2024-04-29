from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get("/items/")
async def get_items(q : Annotated[str | None, Query(max_length=5)] = None):
    res = {"items" : [{"item_id" : "foo"},{"item_id" : "bar"} ]}
    if q : 
        res.update({"q" : q})
    return res