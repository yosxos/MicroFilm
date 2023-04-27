from pydantic import BaseModel
from typing import List, Optional


class GroupIn(BaseModel):
    name: str


class GroupOut(BaseModel):
    id : int
    name:str


