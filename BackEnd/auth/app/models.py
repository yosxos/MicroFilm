from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import (Column, Integer, MetaData, String, Table, Float, create_engine, ARRAY)



class User(BaseModel):
    email: str
    password: str





