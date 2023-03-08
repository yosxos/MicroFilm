from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import (Column, Integer, MetaData, String, Table, Float, create_engine, ARRAY)
from sqlalchemy.ext.declarative import declarative_base



class User(BaseModel):
    email: str
    password: str

class UserInDb(BaseModel):
    id: int
    username: str
    password:str
    token: str


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    token = Column(String)
  

    
