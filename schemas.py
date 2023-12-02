from pydantic import BaseModel
from typing import List, Optional

class PokedexBase(BaseModel):
    pokedex_num: int
    name: str
    description: str
    types: List[str]
    abilities: List[str]
    location: str


class UpdatePokedexBase(BaseModel):
    pokedex_num: Optional[int]
    name: Optional[str]
    description: Optional[str]
    types: Optional[List[str]]
    abilities: Optional[List[str]]
    location: Optional[str]