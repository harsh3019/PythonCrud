from fastapi import FastAPI,HTTPException
from application.crud import crud_router

app = FastAPI()

app.include_router(crud_router, prefix="/item/crud", tags=["crud"])
# items = {}

# @app.post('/item/{item_id}')
# def  create_item(item_id :int,name:str):
#     if item_id in items:
#         raise HTTPException (status_code=404,detail="Id not found")
#     items[item_id] = {name:name}
#     return {"message": "item has been created", "items": {name:name}}

# #read item by usimg item_id

# @app.get('/items/{item_id}')
# async def get_items_id(item_id:int):
#     if item_id not in items:
#         raise HTTPException(status_code=404,detail='Id not found!')
#     return items[item_id]

# @app.get('/items')
# async def get_items():

#     return items

# @app.put('/items/{item_id}')
# async def update_item(item_id:int,name:str):
#     if item_id not in items:
#         raise HTTPException(status_code=404,detail="Id not found")
#     items[item_id]["name"] = name
#     return {"update Item": {name:name}}

# @app.delete('/items/{item_id}')
# async def delete_items(item_id:int):
#     if item_id not in items:
#         raise HTTPException(status_code=404, detail="id not found")
#     del items[item_id]
#     return {"messgae":"Item deleted successfully"}