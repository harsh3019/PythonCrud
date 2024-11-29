from fastapi import FastAPI,HTTPException
from application.crud import crud_router

app = FastAPI()

app.include_router(crud_router, prefix="/item/crud", tags=["crud"])
