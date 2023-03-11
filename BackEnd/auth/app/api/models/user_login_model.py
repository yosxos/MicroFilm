from pydantic import BaseModel
from typing import List, Optional



class User(BaseModel):
    email: str
    password: str





