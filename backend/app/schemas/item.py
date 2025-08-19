"""Pydantic schemas for Item model."""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class ItemBase(BaseModel):
    """Base schema for Item."""
    name: str = Field(..., min_length=1, max_length=255, description="Item name")
    description: Optional[str] = Field(None, description="Item description")

class ItemCreate(ItemBase):
    """Schema for creating a new item."""
    pass

class ItemUpdate(BaseModel):
    """Schema for updating an existing item."""
    name: Optional[str] = Field(None, min_length=1, max_length=255, description="Item name")
    description: Optional[str] = Field(None, description="Item description")

class ItemResponse(ItemBase):
    """Schema for item response."""
    id: int
    created_at: datetime
    
    model_config = {"from_attributes": True}