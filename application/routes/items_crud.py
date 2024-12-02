from fastapi import FastAPI,APIRouter,Depends,HTTPException
from application.models.item import Base,Item
from application.core.db import engine,SessionLocal,get_db
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

item_router = APIRouter()

@item_router.post('/create/item')
def create_item(name:str,description:str,price:float, db: Session = Depends(get_db)):
    new_item = Item(name=name,description=description,price=price)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@item_router.get('/items/get')
async def get_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Item).offset(skip).limit(limit).all()

@item_router.get('/items/{item_id}')
async def get_item_id(item_id:int,db:Session =Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()

    if not item:
        raise HTTPException(status_code=404,detail="Item not found ")
    return item

@item_router.put('/items/update/{item_id}')
async def get_item_update(item_id:int,name:str,description:str,price:float,db :Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()

    if not item:
        raise HTTPException(status_code=404,detail="Item not found,Phirse check kar")
    item.name = name
    item.description = description
    item.price = price
    db.commit()
    db.refresh(item)
    return item

@item_router.delete('/item/delete/{item_id}')
async def item_delete(item_id :int,db:Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()

    if not item:
        raise HTTPException(status_code=404,detail="User not found,Kya tubi re ")
    
    db.delete(item)
    db.commit()
    return  {"message" : "Item deleted successfully"}