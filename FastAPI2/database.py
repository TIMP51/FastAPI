from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import  Column, Integer, String
 
from fastapi import FastAPI
 
SQLALCHEMY_DATABASE_URL = "sqlite:///C:/Users/karat/Desktop/FastAPI2/test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
 
 
Base = declarative_base()
class Person(Base):
    __tablename__ = "people"
 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer, index=True)
 
SessionLocal = sessionmaker(autoflush=False, bind=engine)