from fastapi import FastAPI,Path, Query
from pydantic import BaseModel
from typing import Union, Annotated

app = FastAPI()

class Item(BaseModel):
    name : str
    desc : Union[str, None] = None
    price : float
    tax : Union[float, None] = None

class User(BaseModel):
    username: str
    full_name: Union[str, None] = None

@app.put("/items/{item_id}")
async def update_item(
    item_id : Annotated[int, Path(title="ID Item", ge=1, le = 100)],
    q : Annotated[Union[str, None], Query()] = None,
    item : Union[Item, None] = None,
    user : Union[User, None] = None
) :
    result = {"item_id" : item_id}
    if user :
        result.update({"user" : user})
    if q :
        result.update({"q" : q})
    if item :
        result.update({"item" : item})
    return result