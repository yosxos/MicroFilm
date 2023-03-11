from pydantic import BaseModel
from typing import List, Optional

class MovieIn(BaseModel):
    movie_id: int
    liked: bool
    watched: bool
