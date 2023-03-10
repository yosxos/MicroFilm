from pydantic import BaseModel
from typing import List, Optional

class MovieIn(BaseModel):
    liked: bool
    watched: bool