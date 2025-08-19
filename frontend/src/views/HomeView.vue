<template>
  <div class="home">
    <div class="hero">
      <h1>FastAPI CRUD Application</h1>
      <p class="hero-subtitle">
        A modern full-stack application built with FastAPI and Vue.js 3
      </p>
      <div class="hero-actions">
        <RouterLink to="/items" class="btn btn-primary btn-large">
          <span class="icon">📋</span>
          View Items
        </RouterLink>
        <RouterLink to="/items/create" class="btn btn-secondary btn-large">
          <span class="icon">➕</span>
          Create Item
        </RouterLink>
      </div>
    </div>

    <div class="features">
      <div class="features-grid">
        <div class="feature-card">
          <div class="feature-icon">🚀</div>
          <h3>FastAPI Backend</h3>
          <p>Async SQLAlchemy, PostgreSQL, and automatic API documentation</p>
        </div>
        
        <div class="feature-card">
          <div class="feature-icon">⚡</div>
          <h3>Vue.js 3 Frontend</h3>
          <p>Composition API, TypeScript, and modern reactive state management</p>
        </div>
        
        <div class="feature-card">
          <div class="feature-icon">🔧</div>
          <h3>Full CRUD Operations</h3>
          <p>Create, read, update, and delete items with comprehensive validation</p>
        </div>
        
        <div class="feature-card">
          <div class="feature-icon">📡</div>
          <h3>REST API</h3>
          <p>RESTful endpoints with proper HTTP methods and status codes</p>
        </div>
      </div>
    </div>

    <div class="stats">
      <div class="stats-container">
        <div class="stat-item">
          <div class="stat-value">{{ itemsStore.items.length }}</div>
          <div class="stat-label">Total Items</div>
        </div>
        <div class="stat-item">
          <div class="stat-value">{{ recentItemsCount }}</div>
          <div class="stat-label">Recent Items</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { useItemsStore } from '@/stores/items'

const itemsStore = useItemsStore()

const recentItemsCount = computed(() => {
  const oneDayAgo = new Date()
  oneDayAgo.setDate(oneDayAgo.getDate() - 1)
  
  return itemsStore.items.filter(item => 
    new Date(item.created_at) > oneDayAgo
  ).length
})

onMounted(() => {
  itemsStore.fetchItems()
})
</script>

<style scoped>
.home {
  min-height: 100vh;
}

.hero {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 4rem 2rem;
  text-align: center;
}

.hero h1 {
  font-size: 3rem;
  margin: 0 0 1rem;
  font-weight: 700;
}

.hero-subtitle {
  font-size: 1.25rem;
  margin: 0 0 3rem;
  opacity: 0.9;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.hero-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 0.5rem;
  text-decoration: none;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-large {
  padding: 1rem 2rem;
  font-size: 1.1rem;
}

.btn-primary {
  background: rgba(255, 255, 255, 0.2);
  color: white;
  border: 2px solid rgba(255, 255, 255, 0.3);
}

.btn-primary:hover {
  background: rgba(255, 255, 255, 0.3);
  border-color: rgba(255, 255, 255, 0.5);
}

.btn-secondary {
  background: transparent;
  color: white;
  border: 2px solid rgba(255, 255, 255, 0.5);
}

.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: white;
}

.icon {
  font-size: 1.25rem;
}

.features {
  padding: 4rem 2rem;
  background: #f8f9fa;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.feature-card {
  background: white;
  padding: 2rem;
  border-radius: 0.75rem;
  text-align: center;
  border: 1px solid #e1e8ed;
  transition: transform 0.2s, box-shadow 0.2s;
}

.feature-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
}

.feature-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.feature-card h3 {
  margin: 0 0 1rem;
  color: #2c3e50;
}

.feature-card p {
  margin: 0;
  color: #7f8c8d;
  line-height: 1.6;
}

.stats {
  padding: 2rem;
  background: white;
  border-top: 1px solid #e1e8ed;
}

.stats-container {
  display: flex;
  gap: 2rem;
  justify-content: center;
  max-width: 800px;
  margin: 0 auto;
}

.stat-item {
  text-align: center;
  padding: 1rem;
}

.stat-value {
  font-size: 2.5rem;
  font-weight: 700;
  color: #3498db;
  margin-bottom: 0.5rem;
}

.stat-label {
  color: #7f8c8d;
  font-weight: 500;
  text-transform: uppercase;
  font-size: 0.875rem;
  letter-spacing: 0.05em;
}

@media (max-width: 768px) {
  .hero {
    padding: 2rem 1rem;
  }

  .hero h1 {
    font-size: 2rem;
  }

  .hero-subtitle {
    font-size: 1rem;
  }

  .hero-actions {
    flex-direction: column;
    align-items: center;
  }

  .features {
    padding: 2rem 1rem;
  }

  .features-grid {
    grid-template-columns: 1fr;
  }

  .stats-container {
    flex-direction: column;
    gap: 1rem;
  }
}
</style>
