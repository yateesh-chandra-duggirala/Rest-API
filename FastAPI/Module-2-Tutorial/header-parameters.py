from fastapi import FastAPI, Header
from typing import Union, Annotated

app = FastAPI()

@app.get("/items/")
async def get_items(user_agent : Annotated[Union[str, None],Header()] = None):
    return {"User-Agent" : user_agent}

# Inorder to pass the headers, From the Postman header just give another Key Value pair.
# Such that The parameters would be overridden.

@app.get("/itemsheaders/")
async def get_items(strange_header : Annotated[Union[str, None], Header(convert_underscores= True)] = None):
    return {"strange_header" : strange_header}

# If we keep convert_underscores as False, we will not get the hyphens converted as underscores