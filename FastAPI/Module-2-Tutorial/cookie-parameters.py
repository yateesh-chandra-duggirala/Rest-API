from fastapi import FastAPI, Cookie
from typing import Union
from typing import Annotated

app = FastAPI()

@app.get("/items/")
async def read_items(ads_id : Annotated[Union[str, None], Cookie()] = None):
    return {"ads_id" : ads_id}

# For passing Cookies, we need to pass through Postman as  : 
# Go to Headers in Postman 
# In Key - Value Pair : Key - Cookie, value - ads_id="123"