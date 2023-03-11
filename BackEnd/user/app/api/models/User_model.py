from pydantic import BaseModel
from typing import List, Optional



class UserIn(BaseModel):
    email: str
    password: str
    name: str


class UserOut(BaseModel):
    email: str
    name: str


