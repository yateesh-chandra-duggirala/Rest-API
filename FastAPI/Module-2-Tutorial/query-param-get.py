from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def get_items(q : str | None = None ):
    res = {"items" : [{"item_id" : "foo"},{"item_id" : "bar"} ]}
    if q : 
        res.update({"q" : q})
    return res