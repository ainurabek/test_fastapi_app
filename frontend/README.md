# Vue.js 3 Frontend

A modern Vue.js 3 frontend application with TypeScript, providing a complete CRUD interface for the FastAPI backend.

## Features

- **Vue.js 3** with Composition API
- **TypeScript** for type safety
- **Vue Router** for navigation
- **Pinia** for state management
- **Axios** for API communication
- **Vite** for fast development and building
- Responsive design with modern CSS
- Loading states and error handling
- Form validation

## Project Structure

```
frontend/
├── src/
│   ├── components/          # Reusable Vue components
│   ├── views/              # Page-level components
│   │   ├── HomeView.vue    # Home/landing page
│   │   ├── ItemsView.vue   # List all items
│   │   ├── CreateItemView.vue  # Create new item
│   │   ├── ItemDetailView.vue  # View item details
│   │   ├── EditItemView.vue    # Edit item
│   │   └── AboutView.vue   # About page
│   ├── router/             # Vue Router configuration
│   ├── stores/             # Pinia stores
│   │   └── items.ts        # Items state management
│   ├── services/           # API services
│   │   └── api.ts          # Axios API client
│   ├── assets/             # Static assets
│   ├── App.vue            # Main app component
│   └── main.ts            # App entry point
├── public/                 # Public static files
├── package.json           # Dependencies and scripts
├── vite.config.ts         # Vite configuration
├── tsconfig.json          # TypeScript configuration
└── .env.example           # Environment variables example
```

## Installation & Setup

### Prerequisites

- Node.js 18+
- npm or yarn

### 1. Install Dependencies

```bash
cd frontend
npm install
```

### 2. Environment Configuration

Copy the example environment file and configure your API base URL:

```bash
cp .env.example .env
```

Edit `.env` file:

```env
VITE_API_BASE_URL=http://localhost:8000
```

### 3. Development Server

Start the development server:

```bash
npm run dev
```

The application will be available at:
- **Development**: http://localhost:5173
- **Network**: http://192.168.x.x:5173 (if accessible)

## Available Scripts

### Development
```bash
npm run dev          # Start development server
npm run format       # Format code with Prettier
npm run lint         # Run ESLint
```

### Production
```bash
npm run build        # Build for production
npm run preview      # Preview production build
```

### Type Checking
```bash
npm run type-check   # Run TypeScript type checking
```

## Features Overview

### 🏠 Home Page
- Welcome page with application overview
- Quick navigation to items
- Live statistics display
- Feature highlights

### 📋 Items Management
- **List View**: Display all items with pagination
- **Create**: Add new items with validation
- **View**: Detailed item information
- **Edit**: Update existing items
- **Delete**: Remove items with confirmation

### 🎨 User Interface
- Modern, responsive design
- Loading indicators for async operations
- Error handling with user-friendly messages
- Form validation with real-time feedback
- Breadcrumb navigation
- Mobile-friendly interface

### 🔧 State Management
- Centralized state with Pinia stores
- Reactive data with Vue 3 Composition API
- Optimistic updates for better UX
- Error state management

## API Integration

The frontend communicates with the FastAPI backend through:

### Base Configuration
```typescript
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'
```

### Endpoints Used
| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/items/` | Fetch all items |
| POST | `/api/v1/items/` | Create new item |
| GET | `/api/v1/items/{id}` | Get item details |
| PUT | `/api/v1/items/{id}` | Update item |
| DELETE | `/api/v1/items/{id}` | Delete item |

### Error Handling
- Network errors
- HTTP status errors
- Validation errors
- User-friendly error messages

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `VITE_API_BASE_URL` | Backend API base URL | `http://localhost:8000` |

### Vite Configuration

The application uses Vite for fast development and optimized builds:

- Hot Module Replacement (HMR)
- TypeScript support
- CSS preprocessing
- Code splitting
- Tree shaking

## Development Guidelines

### Code Style
- TypeScript for type safety
- Composition API over Options API
- Single File Components (SFC)
- CSS Modules or scoped styles
- ESLint + Prettier for code formatting

### Component Structure
```vue
<template>
  <!-- Template with semantic HTML -->
</template>

<script setup lang="ts">
// TypeScript logic with Composition API
</script>

<style scoped>
/* Scoped CSS styles */
</style>
```

### State Management
- Use Pinia stores for global state
- Keep component state local when possible
- Use computed properties for derived state
- Handle async operations in stores

## Building for Production

### Build Process
```bash
npm run build
```

This creates optimized files in the `dist/` directory:
- Minified JavaScript and CSS
- Code splitting for lazy-loaded routes
- Asset optimization
- Type checking

### Deployment
The built files can be served by any static file server:
- Nginx
- Apache
- Vercel
- Netlify
- GitHub Pages

### Example Nginx Configuration
```nginx
server {
    listen 80;
    server_name your-domain.com;
    root /path/to/dist;
    index index.html;
    
    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Performance Features

- Code splitting by routes
- Lazy loading of components
- Optimized bundle size
- Tree shaking for unused code
- CSS purging in production

## Troubleshooting

### Common Issues

1. **API Connection Failed**
   - Check if backend is running on correct port
   - Verify `VITE_API_BASE_URL` in `.env`
   - Check CORS configuration in backend

2. **Build Errors**
   - Run `npm run type-check` to check TypeScript errors
   - Clear node_modules and reinstall dependencies

3. **Development Server Issues**
   - Check port availability (default: 5173)
   - Clear browser cache
   - Restart development server
