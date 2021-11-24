from fastapi import FastAPI,Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
	name: str
	price: float
	brand: Optional[str] = None

class UpdateItems(BaseModel):
	name: Optional[str] = None
	price: Optional[float] = None
	brand: Optional[str] = None

inventory = {}

# path/endpoint parameters

@app.get("/get-item/{item_id}")

def get_item(item_id: int = Path(None,description="The ID of the item you want to get")):
	return inventory[item_id]

# ? denotes query parameters

@app.get("/get-by-name")

def get_item(name: str = Query(None, title="Name",description="Name of items.")):
	for item_id in inventory:
		if inventory[item_id]["name"] == name:
			return inventory[item_id]

	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

# request body and POST method

@app.post("/create-item/{item_id}")

def create_item(item_id: int, item: Item):
	if item_id in inventory:
		return {"Error": "Item ID already exists."}

	inventory[item_id] = {"name": item.name, "brand":item.brand, "price": item.price}

	return inventory[item_id]

# update method

@app.put("/update_item/{item_id")

def update_item(item_id:int, item: UpdateItems):
	if item_id not in inventory:
		return {"Error": "Item ID does not exist"}

	if item.name != None:
		inventory[item_id].name = item.names

	if item.name != None:
		inventory[item_id].price = item.price

	if item.name != None:
		inventory[item_id].brand = item.brand

	return inventory[item_id]

# delete items

@app.delete("/delete-items")

def delete_items(item_id: int = Query(...,description="The ID of the item to delete")):
	if item_id not in inventory:
		return {"Error": "ID does not exist"}


	del inventory[item_id]



