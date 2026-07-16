"""
File to handle FastAPI. This is a simple FAST API application that demonstrates basic CRUD operations on a list of items.
Each item has a text and a boolean indicating if it is done or not.
"""
# Pip Imports
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Query, status


app = FastAPI()

class Item(BaseModel):
    text: str | None = None
    is_done: bool = False


ITEMS = []


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items", response_model=list[Item])
def list_items(limit: int = Query(default=10, ge=1, le=100)) -> list[Item]:
    return ITEMS[0: limit]


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < 0 or item_id >= len(ITEMS):
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

    item = ITEMS[item_id]
    return item


@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: Item) -> Item:
    ITEMS.append(item)
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item) -> Item:
    if item_id < 0 or item_id >= len(ITEMS):
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    ITEMS[item_id] = item
    return item


@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int) -> Item:
    if item_id < 0 or item_id >= len(ITEMS):
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    deleted_item = ITEMS.pop(item_id)
    return deleted_item
