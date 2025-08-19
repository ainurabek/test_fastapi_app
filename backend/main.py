"""Main FastAPI application."""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.routers import items

# Load environment variables
load_dotenv()

# Application metadata
app_title = os.getenv("APP_TITLE", "FastAPI CRUD Application")
app_version = os.getenv("APP_VERSION", "1.0.0")
debug = os.getenv("DEBUG", "False").lower() == "true"

# Create FastAPI application
app = FastAPI(
    title=app_title,
    version=app_version,
    description="A full-stack CRUD application with FastAPI backend and Vue.js frontend",
    debug=debug,
)

# Configure CORS for Vue.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173", "http://127.0.0.1:3000", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(items.router, prefix="/api/v1")

@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Welcome to FastAPI CRUD Application",
        "docs": "/docs",
        "version": app_version
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "version": app_version}

if __name__ == "__main__":
    import uvicorn
    
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=debug
    )