# FastAPI Backend

A modern FastAPI application with async SQLAlchemy, PostgreSQL, and full CRUD operations for Items.

## Features

- **FastAPI** with automatic OpenAPI/Swagger documentation
- **SQLAlchemy 2.0+** with async support
- **PostgreSQL** with asyncpg driver
- **Alembic** for database migrations
- **Pydantic** for data validation
- **CORS** middleware for frontend integration
- **Pytest** for testing
- Clean architecture with separate layers (routers, models, schemas, services)

## Project Structure

```
backend/
├── app/
│   ├── database/
│   │   └── database.py          # Database configuration and session management
│   ├── models/
│   │   └── item.py              # SQLAlchemy models
│   ├── schemas/
│   │   └── item.py              # Pydantic schemas
│   ├── routers/
│   │   └── items.py             # API endpoints
│   ├── services/
│   │   └── item_service.py      # Business logic layer
│   └── __init__.py
├── alembic/
│   ├── versions/
│   │   └── 001_initial.py       # Database migration
│   └── env.py                   # Alembic configuration
├── tests/
│   ├── conftest.py              # Test configuration
│   └── test_items.py            # API tests
├── main.py                      # FastAPI application
├── requirements.txt             # Python dependencies
├── alembic.ini                  # Alembic configuration
└── .env.example                 # Environment variables example
```

## Installation & Setup

### Prerequisites

- Python 3.11+
- PostgreSQL database

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Environment Configuration

Copy the example environment file and configure your database:

```bash
cp .env.example .env
```

Edit `.env` file with your database configuration:

```env
DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/fastapi_db
APP_TITLE=FastAPI CRUD Application
APP_VERSION=1.0.0
DEBUG=True
HOST=0.0.0.0
PORT=8000
```

### 3. Database Setup

#### Install PostgreSQL

If PostgreSQL is not already installed on your system:

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

**macOS (using Homebrew):**
```bash
brew install postgresql
brew services start postgresql
```

**Windows:**
Download and install from [PostgreSQL official website](https://www.postgresql.org/download/windows/)

#### Create Database User and Database

1. **Connect to PostgreSQL as superuser:**
```bash
sudo -u postgres psql
```

2. **Create a new user (replace 'username' and 'password' with your preferred credentials):**
```sql
CREATE USER username WITH PASSWORD 'password';
```

3. **Create the database:**
```sql
CREATE DATABASE fastapi_db OWNER username;
```

4. **Grant privileges to the user:**
```sql
GRANT ALL PRIVILEGES ON DATABASE fastapi_db TO username;
```

5. **Exit PostgreSQL:**
```sql
\q
```

#### Update Environment Configuration

Make sure your `.env` file matches the database credentials you just created:

```env
DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/fastapi_db
```

Replace `username` and `password` with the actual credentials you created above.

#### Verify Database Connection

Test the connection (optional but recommended):

```bash
psql -h localhost -U username -d fastapi_db
```

You should be able to connect without errors. Type `\q` to exit.

#### Run Database Migrations

Once the database is set up and accessible, run Alembic migrations to create the tables:

```bash
# Run database migrations
alembic upgrade head
```

This will create all the necessary tables for the application.

### 4. Run the Application

```bash
# Development server with auto-reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Or using Python
python main.py
```

The API will be available at:
- **Application**: http://localhost:8000
- **Interactive API docs**: http://localhost:8000/docs
- **ReDoc documentation**: http://localhost:8000/redoc

## API Endpoints

### Items CRUD

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/items/` | List all items (with pagination) |
| POST | `/api/v1/items/` | Create a new item |
| GET | `/api/v1/items/{id}` | Get item by ID |
| PUT | `/api/v1/items/{id}` | Update item by ID |
| DELETE | `/api/v1/items/{id}` | Delete item by ID |

### Other Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root endpoint |
| GET | `/health` | Health check |
| GET | `/docs` | Interactive API documentation |

## Item Model

```python
{
    "id": 1,
    "name": "Sample Item",
    "description": "This is a sample item",
    "created_at": "2024-01-01T12:00:00Z"
}
```

### Fields

- **id**: Integer, auto-increment primary key
- **name**: String (required, max 255 characters)
- **description**: String (optional, text field)
- **created_at**: DateTime (auto-generated)

## Testing

Run the test suite:

```bash
# Run all tests
PYTHONPATH=. pytest tests/ -v

# Run with coverage
PYTHONPATH=. pytest tests/ --cov=app
```

## Database Migrations

### Create a new migration

```bash
alembic revision --autogenerate -m "Description of changes"
```

### Apply migrations

```bash
alembic upgrade head
```

### Rollback migrations

```bash
alembic downgrade -1
```

## Development

### Code Quality

The project follows these standards:

- **PEP 8** for Python code style
- **Type hints** for all functions
- **Async/await** for I/O operations
- **Clean architecture** with separation of concerns
- **Comprehensive testing** with pytest

### API Documentation

FastAPI automatically generates interactive documentation:

- Visit `/docs` for Swagger UI
- Visit `/redoc` for ReDoc interface
- OpenAPI spec available at `/openapi.json`

## Production Deployment

For production deployment:

1. Set `DEBUG=False` in environment variables
2. Use a production WSGI server like Gunicorn with Uvicorn workers:

```bash
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

3. Set up proper database connection pooling
4. Configure logging and monitoring
5. Use environment variables for sensitive configuration

## CORS Configuration

The application is configured to allow requests from common frontend development ports:

- `http://localhost:3000` (React default)
- `http://localhost:5173` (Vite default)
- `http://127.0.0.1:3000`
- `http://127.0.0.1:5173`

Update the CORS configuration in `main.py` if you need different origins.