<template>
  <div class="items-view">
    <header class="header">
      <h1>Items</h1>
      <RouterLink to="/items/create" class="btn btn-primary">
        <span class="icon">+</span>
        Create New Item
      </RouterLink>
    </header>

    <!-- Loading State -->
    <div v-if="itemsStore.loading" class="loading">
      <div class="spinner"></div>
      <p>Loading items...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="itemsStore.error" class="error">
      <h3>Error</h3>
      <p>{{ itemsStore.error }}</p>
      <button @click="retryLoad" class="btn btn-secondary">Try Again</button>
    </div>

    <!-- Items List -->
    <div v-else class="items-container">
      <div v-if="itemsStore.sortedItems.length === 0" class="empty-state">
        <h3>No Items Found</h3>
        <p>Get started by creating your first item.</p>
        <RouterLink to="/items/create" class="btn btn-primary">Create Item</RouterLink>
      </div>

      <div v-else class="items-grid">
        <div
          v-for="item in itemsStore.sortedItems"
          :key="item.id"
          class="item-card"
        >
          <div class="item-header">
            <h3>{{ item.name }}</h3>
            <div class="item-actions">
              <RouterLink :to="`/items/${item.id}`" class="btn btn-sm btn-outline">
                View
              </RouterLink>
              <RouterLink :to="`/items/${item.id}/edit`" class="btn btn-sm btn-secondary">
                Edit
              </RouterLink>
              <button @click="handleDelete(item)" class="btn btn-sm btn-danger">
                Delete
              </button>
            </div>
          </div>
          
          <div class="item-content">
            <p v-if="item.description" class="description">{{ item.description }}</p>
            <p v-else class="no-description">No description</p>
            <p class="created-at">Created: {{ formatDate(item.created_at) }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Delete Confirmation Modal -->
    <div v-if="itemToDelete" class="modal-overlay" @click="cancelDelete">
      <div class="modal" @click.stop>
        <h3>Confirm Delete</h3>
        <p>Are you sure you want to delete "{{ itemToDelete.name }}"?</p>
        <div class="modal-actions">
          <button @click="cancelDelete" class="btn btn-secondary">Cancel</button>
          <button @click="confirmDelete" class="btn btn-danger" :disabled="itemsStore.loading">
            {{ itemsStore.loading ? 'Deleting...' : 'Delete' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { RouterLink } from 'vue-router'
import { useItemsStore } from '@/stores/items'
import type { Item } from '@/services/api'

const itemsStore = useItemsStore()
const itemToDelete = ref<Item | null>(null)

onMounted(() => {
  itemsStore.fetchItems()
})

function formatDate(dateString: string): string {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

function handleDelete(item: Item) {
  itemToDelete.value = item
}

function cancelDelete() {
  itemToDelete.value = null
}

async function confirmDelete() {
  if (itemToDelete.value) {
    const success = await itemsStore.deleteItem(itemToDelete.value.id)
    if (success) {
      itemToDelete.value = null
    }
  }
}

function retryLoad() {
  itemsStore.clearError()
  itemsStore.fetchItems()
}
</script>

<style scoped>
.items-view {
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.header h1 {
  margin: 0;
  color: #2c3e50;
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

.btn-primary {
  background: #3498db;
  color: white;
}

.btn-primary:hover {
  background: #2980b9;
}

.btn-secondary {
  background: #95a5a6;
  color: white;
}

.btn-secondary:hover {
  background: #7f8c8d;
}

.btn-outline {
  background: transparent;
  color: #3498db;
  border: 1px solid #3498db;
}

.btn-outline:hover {
  background: #3498db;
  color: white;
}

.btn-danger {
  background: #e74c3c;
  color: white;
}

.btn-danger:hover {
  background: #c0392b;
}

.btn-sm {
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
}

.icon {
  font-size: 1.25rem;
}

.loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  padding: 4rem;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #f3f3f3;
  border-top: 4px solid #3498db;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.error {
  text-align: center;
  padding: 2rem;
  color: #e74c3c;
}

.empty-state {
  text-align: center;
  padding: 4rem;
  color: #7f8c8d;
}

.items-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 1.5rem;
}

.item-card {
  background: white;
  border: 1px solid #e1e8ed;
  border-radius: 0.75rem;
  overflow: hidden;
  transition: transform 0.2s, box-shadow 0.2s;
}

.item-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.item-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1rem;
  padding: 1.5rem 1.5rem 1rem;
  border-bottom: 1px solid #f8f9fa;
}

.item-header h3 {
  margin: 0;
  color: #2c3e50;
  flex: 1;
}

.item-actions {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.item-content {
  padding: 1rem 1.5rem 1.5rem;
}

.description {
  margin: 0 0 1rem;
  color: #555;
  line-height: 1.5;
}

.no-description {
  margin: 0 0 1rem;
  color: #aaa;
  font-style: italic;
}

.created-at {
  margin: 0;
  font-size: 0.875rem;
  color: #7f8c8d;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal {
  background: white;
  padding: 2rem;
  border-radius: 0.75rem;
  max-width: 400px;
  width: 90%;
}

.modal h3 {
  margin: 0 0 1rem;
  color: #2c3e50;
}

.modal p {
  margin: 0 0 2rem;
  color: #555;
}

.modal-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
}

@media (max-width: 768px) {
  .items-view {
    padding: 1rem;
  }

  .header {
    flex-direction: column;
    gap: 1rem;
    align-items: stretch;
  }

  .items-grid {
    grid-template-columns: 1fr;
  }

  .item-header {
    flex-direction: column;
    gap: 1rem;
  }

  .item-actions {
    justify-content: flex-start;
  }
}
</style>