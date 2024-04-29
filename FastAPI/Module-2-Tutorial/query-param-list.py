from fastapi import FastAPI, Query
from typing import Annotated, Union, List

app = FastAPI()

@app.get("/items/")
async def get_item_list(q : Annotated[Union[List[str], None], Query()] = ["Loo", "Foo"]):
    result = {"item" : f"{q}"}
    return result