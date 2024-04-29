from fastapi import FastAPI, Path, Query
from typing import Union, Annotated

app = FastAPI()

@app.get("/item/{item_id}")
async def read_item(
    *,
    item_id : Annotated[int, Path(title="ID of Item", ge=2)],
    q : Annotated[Union[str, None], Query(alias="item-query")] = None,
    size : Annotated[float, Query(gt = 0, lt = 10.5)]
):
    results = {"item_id" : item_id, "size" : size}
    if q : 
        results.update({"q" : q})
    return results