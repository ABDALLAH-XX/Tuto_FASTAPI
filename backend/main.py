from fastapi import FastAPI 

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]

@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]

@app.get("/users")
async def read_users3():
    return ["Bozo", "Man"]

# The first @get will always be used since the path matches first
# Even though read_users3 is displayed on the web page