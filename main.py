from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

inventory = {}


class ItemUpdate(BaseModel):
    name: Optional[str] = None
    lname: Optional[str] = None


class Item(BaseModel):
    name: str
    lname: str


@app.get("/")
def home():
    return {"Welcome": "Home"}


@app.get("/get-user-id")
def get_user_id(user_id: Optional[int] = None):
    if user_id in inventory:
        return inventory[user_id]
    raise HTTPException(status_code=404, detail="Im lost")


@app.get("/get-by-name")
def get_user_name(name: str):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code=400, detail=f"{name} not found!")


@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Already Exists"}
    else:
        inventory[item_id] = item
        return inventory[item_id]


@app.put("/update-item")
def update_item(item_id: int, item: ItemUpdate):
    if item_id not in inventory:
        raise HTTPException(status_code=400, detail="wouchire")

    if item.name is not None:
        inventory[item_id].name = item.name

    if item.lname is not None:
        inventory[item_id].lname = item.lname
    return inventory[item_id]


@app.delete("/delete-item")
def delete_item(item_id: int):
    if item_id not in inventory:
        raise HTTPException(status_code=400, detail="racxa momcela")

    del inventory[item_id]
    return {"Succes": "item deleted"}
