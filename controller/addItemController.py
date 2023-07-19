from model.Item import Item

async def create_item(item: Item):
    # Insert the item into MongoDB
    collection = db["items"]
    result = collection.insert_one(item.dict())
    return {"id": str(result.inserted_id), "item": item}