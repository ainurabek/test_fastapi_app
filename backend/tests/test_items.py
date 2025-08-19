"""Test the Item API endpoints."""
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_create_item(client: AsyncClient):
    """Test creating a new item."""
    item_data = {
        "name": "Test Item",
        "description": "This is a test item"
    }
    
    response = await client.post("/api/v1/items/", json=item_data)
    assert response.status_code == 201
    
    data = response.json()
    assert data["name"] == item_data["name"]
    assert data["description"] == item_data["description"]
    assert "id" in data
    assert "created_at" in data

@pytest.mark.asyncio
async def test_create_item_without_description(client: AsyncClient):
    """Test creating an item without description."""
    item_data = {
        "name": "Test Item without description"
    }
    
    response = await client.post("/api/v1/items/", json=item_data)
    assert response.status_code == 201
    
    data = response.json()
    assert data["name"] == item_data["name"]
    assert data["description"] is None

@pytest.mark.asyncio
async def test_get_items_empty(client: AsyncClient):
    """Test getting items when database is empty."""
    response = await client.get("/api/v1/items/")
    assert response.status_code == 200
    assert response.json() == []

@pytest.mark.asyncio
async def test_get_items(client: AsyncClient):
    """Test getting all items."""
    # Create some items first
    item1 = {"name": "Item 1", "description": "First item"}
    item2 = {"name": "Item 2", "description": "Second item"}
    
    await client.post("/api/v1/items/", json=item1)
    await client.post("/api/v1/items/", json=item2)
    
    response = await client.get("/api/v1/items/")
    assert response.status_code == 200
    
    data = response.json()
    assert len(data) == 2
    
    # Items should be ordered by created_at desc (newest first)
    assert data[0]["name"] == "Item 2"
    assert data[1]["name"] == "Item 1"

@pytest.mark.asyncio
async def test_get_item_by_id(client: AsyncClient):
    """Test getting a specific item by ID."""
    item_data = {"name": "Test Item", "description": "Test description"}
    
    # Create item
    create_response = await client.post("/api/v1/items/", json=item_data)
    created_item = create_response.json()
    item_id = created_item["id"]
    
    # Get item by ID
    response = await client.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == item_data["name"]
    assert data["description"] == item_data["description"]

@pytest.mark.asyncio
async def test_get_item_not_found(client: AsyncClient):
    """Test getting a non-existent item."""
    response = await client.get("/api/v1/items/999")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()

@pytest.mark.asyncio
async def test_update_item(client: AsyncClient):
    """Test updating an existing item."""
    item_data = {"name": "Original Item", "description": "Original description"}
    
    # Create item
    create_response = await client.post("/api/v1/items/", json=item_data)
    created_item = create_response.json()
    item_id = created_item["id"]
    
    # Update item
    update_data = {"name": "Updated Item", "description": "Updated description"}
    response = await client.put(f"/api/v1/items/{item_id}", json=update_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == update_data["name"]
    assert data["description"] == update_data["description"]

@pytest.mark.asyncio
async def test_update_item_partial(client: AsyncClient):
    """Test partially updating an item."""
    item_data = {"name": "Original Item", "description": "Original description"}
    
    # Create item
    create_response = await client.post("/api/v1/items/", json=item_data)
    created_item = create_response.json()
    item_id = created_item["id"]
    
    # Update only name
    update_data = {"name": "Updated Name Only"}
    response = await client.put(f"/api/v1/items/{item_id}", json=update_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == update_data["name"]
    assert data["description"] == item_data["description"]  # Should remain unchanged

@pytest.mark.asyncio
async def test_update_item_not_found(client: AsyncClient):
    """Test updating a non-existent item."""
    update_data = {"name": "Updated Item"}
    response = await client.put("/api/v1/items/999", json=update_data)
    assert response.status_code == 404

@pytest.mark.asyncio
async def test_delete_item(client: AsyncClient):
    """Test deleting an item."""
    item_data = {"name": "Item to delete", "description": "Will be deleted"}
    
    # Create item
    create_response = await client.post("/api/v1/items/", json=item_data)
    created_item = create_response.json()
    item_id = created_item["id"]
    
    # Delete item
    response = await client.delete(f"/api/v1/items/{item_id}")
    assert response.status_code == 204
    
    # Verify item is deleted
    get_response = await client.get(f"/api/v1/items/{item_id}")
    assert get_response.status_code == 404

@pytest.mark.asyncio
async def test_delete_item_not_found(client: AsyncClient):
    """Test deleting a non-existent item."""
    response = await client.delete("/api/v1/items/999")
    assert response.status_code == 404

@pytest.mark.asyncio
async def test_create_item_validation_error(client: AsyncClient):
    """Test creating an item with validation errors."""
    # Missing required name field
    item_data = {"description": "Item without name"}
    
    response = await client.post("/api/v1/items/", json=item_data)
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_root_endpoint(client: AsyncClient):
    """Test the root endpoint."""
    response = await client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "docs" in data
    assert "version" in data

@pytest.mark.asyncio
async def test_health_check(client: AsyncClient):
    """Test the health check endpoint."""
    response = await client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "version" in data