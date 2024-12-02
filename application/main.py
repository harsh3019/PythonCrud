from fastapi import FastAPI,HTTPException
from application.crud import crud_router
from application.routes.items_crud import item_router
from application.config import root_env
# from models.item import Base

DB_URL = root_env.env_get("DB_URL")
print(DB_URL)


app = FastAPI()

app.include_router(crud_router, prefix="/item/crud", tags=["crud"])
app.include_router(item_router,prefix="/crud",tags=["Item"])
