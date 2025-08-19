"""Item service layer for business logic."""
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from sqlalchemy.exc import NoResultFound
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate

class ItemService:
    """Service class for Item CRUD operations."""
    
    @staticmethod
    async def create_item(db: AsyncSession, item_data: ItemCreate) -> Item:
        """Create a new item."""
        item = Item(**item_data.model_dump())
        db.add(item)
        await db.commit()
        await db.refresh(item)
        return item
    
    @staticmethod
    async def get_item(db: AsyncSession, item_id: int) -> Optional[Item]:
        """Get an item by ID."""
        query = select(Item).where(Item.id == item_id)
        result = await db.execute(query)
        return result.scalar_one_or_none()
    
    @staticmethod
    async def get_items(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Item]:
        """Get all items with pagination."""
        query = select(Item).offset(skip).limit(limit).order_by(Item.created_at.desc())
        result = await db.execute(query)
        return result.scalars().all()
    
    @staticmethod
    async def update_item(db: AsyncSession, item_id: int, item_data: ItemUpdate) -> Optional[Item]:
        """Update an existing item."""
        # First check if item exists
        existing_item = await ItemService.get_item(db, item_id)
        if not existing_item:
            return None
        
        # Update only provided fields
        update_data = item_data.model_dump(exclude_unset=True)
        if not update_data:
            return existing_item
        
        query = update(Item).where(Item.id == item_id).values(**update_data)
        await db.execute(query)
        await db.commit()
        
        # Return updated item
        return await ItemService.get_item(db, item_id)
    
    @staticmethod
    async def delete_item(db: AsyncSession, item_id: int) -> bool:
        """Delete an item by ID."""
        # First check if item exists
        existing_item = await ItemService.get_item(db, item_id)
        if not existing_item:
            return False
        
        query = delete(Item).where(Item.id == item_id)
        await db.execute(query)
        await db.commit()
        return True