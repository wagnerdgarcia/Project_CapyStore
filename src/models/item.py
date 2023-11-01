from pydantic import BaseModel
from typing import List

class ItemCreate(BaseModel):
    name: str
    category: str
    amount: int
    price: float
    manufactured_at: str

class ItemUpdate(BaseModel):
    name: str
    category: str
    amount: int
    price: float
    manufactured_at: str

class ItemResponse(BaseModel):
    name: str
    category: str
    amount: int
    price: float
    manufactured_at: str

class ItemListResponse(BaseModel):
    Itens: List[ItemResponse]