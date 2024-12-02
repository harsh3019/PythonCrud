from sqlalchemy import Column,Integer,String,Float
from sqlalchemy.ext.declarative import declarative_base
from pydantic import field_validator
from fastapi import HTTPException
Base = declarative_base()

class Item(Base):

    __tablename__ = "Items"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(255),index=True,unique=True)
    price = Column(Float,index=True)
    description = Column(String(255),index=True)
    

    @field_validator("price")
    def check_price_value(cls,value):
        if value <=0:
            raise HTTPException(status_code=405, detail="Price must be greater than 0")
        return value


