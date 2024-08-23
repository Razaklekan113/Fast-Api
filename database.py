from sqlalchemy import create_engine # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore

# create database engine
engine = create_engine("sqlite:///todo.db")

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)