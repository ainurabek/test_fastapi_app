# Copilot Instructions for FastAPI Test Application

## Project Overview
This is a test FastAPI application designed to demonstrate modern Python web API development patterns. When working on this project, follow these guidelines to ensure consistent, maintainable, and well-structured code.

## Architecture & Patterns

### Application Structure
- Use the standard FastAPI application structure with clear separation of concerns
- Organize code into modules: `routers/`, `models/`, `schemas/`, `services/`, `database/`
- Keep main application file (`main.py`) clean and focused on app configuration
- Use dependency injection for database connections, authentication, and shared services

### API Design
- Follow RESTful conventions for endpoint design
- Use appropriate HTTP methods (GET, POST, PUT, DELETE, PATCH)
- Implement proper HTTP status codes (200, 201, 400, 404, 422, 500)
- Use Pydantic models for request/response validation
- Implement proper error handling with custom exception handlers
- Include comprehensive API documentation with docstrings

## Code Standards

### Python Style
- Follow PEP 8 style guidelines
- Use type hints for all function parameters and return values
- Prefer async/await for I/O operations
- Use descriptive variable and function names
- Keep functions small and focused on single responsibilities

### FastAPI Specific
- Use `APIRouter` for organizing endpoints into logical groups
- Implement proper dependency injection using `Depends()`
- Use Pydantic `BaseModel` for all request/response schemas
- Implement proper validation with Pydantic validators when needed
- Use `HTTPException` for API error responses
- Include response models in endpoint decorators for documentation

### Database Integration
- Use SQLAlchemy or similar ORM for database operations
- Implement proper database session management
- Use async database drivers when possible (asyncpg, aiomysql)
- Implement database migrations with Alembic
- Follow repository pattern for data access layer

## Testing Strategy

### Test Structure
- Use pytest for all testing
- Organize tests to mirror application structure
- Use `httpx.AsyncClient` for API endpoint testing
- Implement test fixtures for database setup/teardown
- Use factory patterns for test data generation

### Test Types
- Unit tests for business logic and utility functions
- Integration tests for API endpoints
- Database tests with test database isolation
- Authentication and authorization tests
- Performance tests for critical endpoints

## Development Workflow

### Environment Setup
- Use virtual environments (venv or conda)
- Pin dependencies in `requirements.txt` or `pyproject.toml`
- Include development dependencies separately
- Use environment variables for configuration
- Implement proper logging configuration

### Code Quality
- Use linting tools (flake8, pylint, or ruff)
- Implement code formatting with black
- Use import sorting with isort
- Run type checking with mypy
- Include pre-commit hooks for automated checks

## Security Best Practices

### Authentication & Authorization
- Implement JWT token-based authentication
- Use OAuth2 with proper scopes for authorization
- Hash passwords using bcrypt or similar
- Implement rate limiting for sensitive endpoints
- Validate and sanitize all user inputs

### Data Protection
- Use HTTPS in production
- Implement proper CORS configuration
- Validate file uploads thoroughly
- Use parameterized queries to prevent SQL injection
- Log security events appropriately

## API Documentation

### Interactive Documentation
- Leverage FastAPI's automatic OpenAPI/Swagger documentation
- Include comprehensive descriptions for all endpoints
- Provide example requests and responses
- Document error responses and status codes
- Use tags to organize endpoints logically

### Code Documentation
- Include docstrings for all functions and classes
- Document complex business logic inline
- Maintain README with setup and usage instructions
- Document API versioning strategy
- Include deployment and configuration guides

## Performance Considerations

### Optimization
- Use async/await for I/O-bound operations
- Implement proper database query optimization
- Use connection pooling for database connections
- Implement caching strategies where appropriate
- Monitor and log performance metrics

### Monitoring
- Implement health check endpoints
- Use structured logging with correlation IDs
- Monitor response times and error rates
- Implement graceful error handling and recovery
- Use proper status endpoints for load balancers

## Dependencies & Libraries

### Core Dependencies
- FastAPI for web framework
- Pydantic for data validation
- SQLAlchemy for ORM (if using SQL database)
- asyncpg/aiomysql for async database drivers
- pytest for testing framework

### Development Dependencies
- black for code formatting
- flake8/ruff for linting
- mypy for type checking
- httpx for API testing
- pytest-asyncio for async testing

## Example Patterns

When implementing new features, follow these patterns:

### Endpoint Implementation
```python
@router.post("/items/", response_model=ItemResponse, status_code=201)
async def create_item(
    item: ItemCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> ItemResponse:
    """Create a new item with proper validation and error handling."""
    pass
```

### Service Layer
```python
class ItemService:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def create_item(self, item_data: ItemCreate) -> Item:
        """Business logic for item creation."""
        pass
```

### Error Handling
```python
@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()}
    )
```

Remember to always prioritize code readability, maintainability, and testability when implementing new features or refactoring existing code.