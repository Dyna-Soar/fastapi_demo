from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

items_db = [
    {
    "id": 1,
    "name": "orange",
    "price": 2
    }
]


class Item(BaseModel):
    id: int
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/items", response_model=List[Item])
async def read_items():
    return items_db


@app.post("/items", status_code=201)
async def create_item(payload: Item):
    item = payload.dict()
    items_db.append(item)
    return items_db[-1]


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    for item in items_db:
        if item["id"] == item_id:
            return item
    return {"item": "no such item in db"}
