<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div id="app">
    <nav class="navbar">
      <div class="nav-container">
        <RouterLink to="/" class="nav-brand">
          <span class="brand-icon">📋</span>
          FastAPI CRUD
        </RouterLink>
        
        <div class="nav-links">
          <RouterLink to="/" class="nav-link">Home</RouterLink>
          <RouterLink to="/items" class="nav-link">Items</RouterLink>
          <RouterLink to="/items/create" class="nav-link nav-link-primary">Create Item</RouterLink>
        </div>
      </div>
    </nav>

    <main class="main-content">
      <RouterView />
    </main>

    <footer class="footer">
      <div class="footer-container">
        <p>&copy; 2024 FastAPI CRUD Application. Built with FastAPI and Vue.js 3.</p>
      </div>
    </footer>
  </div>
</template>

<style scoped>
#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.navbar {
  background: white;
  border-bottom: 1px solid #e1e8ed;
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 4rem;
}

.nav-brand {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1.25rem;
  font-weight: 700;
  color: #2c3e50;
  text-decoration: none;
}

.brand-icon {
  font-size: 1.5rem;
}

.nav-links {
  display: flex;
  gap: 2rem;
  align-items: center;
}

.nav-link {
  color: #7f8c8d;
  text-decoration: none;
  font-weight: 500;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  transition: all 0.2s;
}

.nav-link:hover {
  color: #2c3e50;
  background: #f8f9fa;
}

.nav-link.router-link-active {
  color: #3498db;
  background: rgba(52, 152, 219, 0.1);
}

.nav-link-primary {
  background: #3498db;
  color: white;
}

.nav-link-primary:hover {
  background: #2980b9;
  color: white;
}

.nav-link-primary.router-link-active {
  background: #2980b9;
  color: white;
}

.main-content {
  flex: 1;
  background: #f8f9fa;
}

.footer {
  background: white;
  border-top: 1px solid #e1e8ed;
  padding: 1.5rem 0;
}

.footer-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  text-align: center;
  color: #7f8c8d;
}

.footer p {
  margin: 0;
  font-size: 0.875rem;
}

@media (max-width: 768px) {
  .nav-container {
    padding: 0 1rem;
    flex-direction: column;
    gap: 1rem;
    height: auto;
    padding-top: 1rem;
    padding-bottom: 1rem;
  }

  .nav-links {
    gap: 1rem;
    flex-wrap: wrap;
    justify-content: center;
  }

  .footer-container {
    padding: 0 1rem;
  }
}
</style>
