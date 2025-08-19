# FastAPI + Vue.js 3 Full-Stack CRUD Application

A modern full-stack web application demonstrating CRUD operations with FastAPI backend and Vue.js 3 frontend.

## 🚀 Features

### Backend (FastAPI)
- **FastAPI** with async SQLAlchemy v2.0+
- **PostgreSQL** database with asyncpg driver
- **Alembic** for database migrations
- **Pydantic** for data validation
- **Pytest** for testing
- Clean architecture with separation of concerns
- Interactive API documentation at `/docs`
- CORS middleware for frontend integration

### Frontend (Vue.js 3)
- **Vue.js 3** with Composition API and TypeScript
- **Vue Router** for navigation
- **Pinia** for state management
- **Axios** for API communication
- **Vite** for fast development and building
- Responsive design with modern CSS
- Loading states and error handling
- Form validation

### Integration
- RESTful API with proper HTTP methods and status codes
- Environment-based configuration
- Independent development servers
- Production-ready build process

## 📋 Item Model

The application manages items with the following structure:

```typescript
interface Item {
  id: number              // Auto-increment primary key
  name: string           // Required, max 255 characters
  description?: string   // Optional text field
  created_at: string     // Auto-generated timestamp
}
```

## 🏗️ Project Structure

```
.
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── database/       # Database configuration
│   │   ├── models/         # SQLAlchemy models
│   │   ├── schemas/        # Pydantic schemas
│   │   ├── routers/        # API endpoints
│   │   └── services/       # Business logic
│   ├── alembic/           # Database migrations
│   ├── tests/             # Backend tests
│   ├── main.py            # FastAPI application
│   ├── requirements.txt   # Python dependencies
│   └── README.md          # Backend documentation
├── frontend/              # Vue.js frontend
│   ├── src/
│   │   ├── views/         # Page components
│   │   ├── stores/        # Pinia stores
│   │   ├── services/      # API services
│   │   └── router/        # Vue Router config
│   ├── package.json       # Node.js dependencies
│   └── README.md          # Frontend documentation
├── .gitignore
└── README.md              # This file
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.11+**
- **Node.js 18+**
- **PostgreSQL** database

### 1. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your PostgreSQL database URL

# Run database migrations
alembic upgrade head

# Start FastAPI server
uvicorn main:app --reload
```

Backend will be available at: http://localhost:8000
- API docs: http://localhost:8000/docs
- Health check: http://localhost:8000/health

### 2. Frontend Setup

```bash
# Navigate to frontend directory (in a new terminal)
cd frontend

# Install Node.js dependencies
npm install

# Configure environment
cp .env.example .env
# Edit .env with your backend URL (default: http://localhost:8000)

# Start development server
npm run dev
```

Frontend will be available at: http://localhost:5173

## 🔧 Development

### Backend Development

```bash
cd backend

# Run tests
PYTHONPATH=. pytest tests/ -v

# Create new migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head

# Run with custom settings
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Frontend Development

```bash
cd frontend

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Run linting
npm run lint

# Format code
npm run format
```

## 📚 API Documentation

### Items Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/items/` | List all items (with pagination) |
| POST | `/api/v1/items/` | Create a new item |
| GET | `/api/v1/items/{id}` | Get item by ID |
| PUT | `/api/v1/items/{id}` | Update item by ID |
| DELETE | `/api/v1/items/{id}` | Delete item by ID |

### Example API Usage

**Create Item:**
```bash
curl -X POST "http://localhost:8000/api/v1/items/" \
  -H "Content-Type: application/json" \
  -d '{"name": "My Item", "description": "Item description"}'
```

**Get All Items:**
```bash
curl "http://localhost:8000/api/v1/items/"
```

**Update Item:**
```bash
curl -X PUT "http://localhost:8000/api/v1/items/1" \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Item"}'
```

## 🌐 Frontend Pages

- **Home** (`/`) - Landing page with app overview
- **Items List** (`/items`) - Display all items with search and pagination
- **Create Item** (`/items/create`) - Form to create new items
- **Item Detail** (`/items/:id`) - View individual item details
- **Edit Item** (`/items/:id/edit`) - Form to edit existing items

## 🔒 Environment Configuration

### Backend (.env)

```env
DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/fastapi_db
APP_TITLE=FastAPI CRUD Application
APP_VERSION=1.0.0
DEBUG=True
HOST=0.0.0.0
PORT=8000
```

### Frontend (.env)

```env
VITE_API_BASE_URL=http://localhost:8000
```

## 🧪 Testing

### Backend Tests

```bash
cd backend
PYTHONPATH=. pytest tests/ -v --cov=app
```

### Frontend Tests

```bash
cd frontend
npm run test        # Unit tests
npm run test:ui     # Test UI
```

## 🚀 Production Deployment

### Backend Deployment

1. Set production environment variables
2. Use a production WSGI server:
   ```bash
   gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
   ```
3. Set up PostgreSQL database
4. Run migrations: `alembic upgrade head`

### Frontend Deployment

1. Build the application:
   ```bash
   npm run build
   ```
2. Serve the `dist/` directory with a static file server
3. Configure your web server for SPA routing

### Docker Deployment (Optional)

Create `docker-compose.yml`:

```yaml
version: '3.8'
services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: fastapi_db
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql+asyncpg://postgres:password@db:5432/fastapi_db
    depends_on:
      - db

  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend

volumes:
  postgres_data:
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Run tests: `pytest` (backend) and `npm test` (frontend)
5. Commit your changes: `git commit -am 'Add feature'`
6. Push to the branch: `git push origin feature-name`
7. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Troubleshooting

### Common Issues

1. **Database Connection Failed**
   - Ensure PostgreSQL is running
   - Check DATABASE_URL in backend `.env`
   - Verify database credentials

2. **CORS Errors**
   - Check frontend URL in backend CORS configuration
   - Verify VITE_API_BASE_URL in frontend `.env`

3. **Migration Errors**
   - Ensure database exists
   - Check Alembic configuration
   - Run `alembic upgrade head`

4. **Frontend Build Errors**
   - Clear node_modules: `rm -rf node_modules && npm install`
   - Check TypeScript errors: `npm run type-check`

For detailed setup instructions, see the README files in the `backend/` and `frontend/` directories.