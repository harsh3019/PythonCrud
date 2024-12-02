# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from application.config.root_env import env_get
# from application.models.item import Base

# DB_URL = env_get("DB_URL")


# print(DB_URL)
# DB_URL = "mysql+pymysql://root:@localhost:3306/python_db"

# engine = create_engine(DB_URL)
# SessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)


from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from application.models.item import Base

import os

# Load environment variables from .env file
load_dotenv()

# Get the DB_URL from the environment variable
DB_URL = os.getenv("DB_URL")

# Create the SQLAlchemy engine using the DB_URL
engine = create_engine(DB_URL)

# Create the SessionLocal class
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

   
Base.metadata.create_all(bind=engine)

    