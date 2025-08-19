"""Item router for API endpoints."""
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.database import get_db
from app.schemas.item import ItemCreate, ItemUpdate, ItemResponse
from app.services.item_service import ItemService

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(
    item: ItemCreate,
    db: AsyncSession = Depends(get_db)
) -> ItemResponse:
    """
    Create a new item.
    
    - **name**: Item name (required)
    - **description**: Item description (optional)
    """
    return await ItemService.create_item(db, item)

@router.get("/", response_model=List[ItemResponse])
async def read_items(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
) -> List[ItemResponse]:
    """
    Get all items with pagination.
    
    - **skip**: Number of items to skip (default: 0)
    - **limit**: Maximum number of items to return (default: 100)
    """
    return await ItemService.get_items(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=ItemResponse)
async def read_item(
    item_id: int,
    db: AsyncSession = Depends(get_db)
) -> ItemResponse:
    """
    Get a specific item by ID.
    
    - **item_id**: ID of the item to retrieve
    """
    item = await ItemService.get_item(db, item_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    return item

@router.put("/{item_id}", response_model=ItemResponse)
async def update_item(
    item_id: int,
    item: ItemUpdate,
    db: AsyncSession = Depends(get_db)
) -> ItemResponse:
    """
    Update an existing item.
    
    - **item_id**: ID of the item to update
    - **name**: New item name (optional)
    - **description**: New item description (optional)
    """
    updated_item = await ItemService.update_item(db, item_id, item)
    if updated_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    return updated_item

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(
    item_id: int,
    db: AsyncSession = Depends(get_db)
) -> None:
    """
    Delete an item.
    
    - **item_id**: ID of the item to delete
    """
    success = await ItemService.delete_item(db, item_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )