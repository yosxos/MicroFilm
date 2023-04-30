from pydantic import BaseModel
from typing import List, Optional

class MovieIn(BaseModel):
    name: str
    overview: str
    release_date:str
    note_average: float
    poster_path:str
    genres_id: List[int]


class MovieOut(MovieIn):
    id: int

class MovieUpdate(MovieIn):
    name: Optional[str] = None
    overview: Optional[str] = None
    genres: Optional[List[int]] = None
    note_average : Optional[float] = None