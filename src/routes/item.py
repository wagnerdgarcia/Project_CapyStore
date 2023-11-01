from fastapi import APIRouter, HTTPException
from src.controllers.item import ItemController
from src.models.item import *  # Importe o modelo Pydantic

router = APIRouter()
controller = ItemController()

@router.post("/", response_model=ItemResponse)
def create(item_data: ItemCreate):
    # Valida os dados da requisição usando o modelo Pydantic
    created_item = controller.create(item_data.dict())
    return created_item

@router.get("/{item_id}", response_model=ItemResponse)
def get(item_id: int):
    item = controller.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/{item_id}", response_model=ItemResponse)
def update(item_id: int, item_data: ItemUpdate):
    # Valida os dados da requisição usando o modelo Pydantic
    updated_item = controller.update(item_id, item_data.dict())
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@router.delete("/{item_id}")
def delete(item_id: int):
    success = controller.delete(item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted"}