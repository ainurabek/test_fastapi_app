<template>
  <div class="item-detail-view">
    <header class="header">
      <div class="breadcrumb">
        <RouterLink to="/items" class="breadcrumb-link">Items</RouterLink>
        <span class="breadcrumb-separator">/</span>
        <span class="breadcrumb-current">{{ item?.name || 'Loading...' }}</span>
      </div>
    </header>

    <!-- Loading State -->
    <div v-if="itemsStore.loading && !item" class="loading">
      <div class="spinner"></div>
      <p>Loading item...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="itemsStore.error" class="error">
      <h3>Error</h3>
      <p>{{ itemsStore.error }}</p>
      <div class="error-actions">
        <button @click="loadItem" class="btn btn-secondary">Try Again</button>
        <RouterLink to="/items" class="btn btn-primary">Back to Items</RouterLink>
      </div>
    </div>

    <!-- Item Details -->
    <div v-else-if="item" class="item-container">
      <div class="item-card">
        <div class="item-header">
          <h1>{{ item.name }}</h1>
          <div class="item-actions">
            <RouterLink :to="`/items/${item.id}/edit`" class="btn btn-primary">
              <span class="icon">✏️</span>
              Edit
            </RouterLink>
            <button @click="showDeleteModal = true" class="btn btn-danger">
              <span class="icon">🗑️</span>
              Delete
            </button>
          </div>
        </div>

        <div class="item-content">
          <div class="field">
            <label class="field-label">ID</label>
            <div class="field-value">{{ item.id }}</div>
          </div>

          <div class="field">
            <label class="field-label">Name</label>
            <div class="field-value">{{ item.name }}</div>
          </div>

          <div class="field">
            <label class="field-label">Description</label>
            <div class="field-value">
              <span v-if="item.description">{{ item.description }}</span>
              <span v-else class="no-value">No description provided</span>
            </div>
          </div>

          <div class="field">
            <label class="field-label">Created At</label>
            <div class="field-value">{{ formatDate(item.created_at) }}</div>
          </div>
        </div>
      </div>

      <div class="back-link">
        <RouterLink to="/items" class="btn btn-secondary">
          <span class="icon">←</span>
          Back to Items
        </RouterLink>
      </div>
    </div>

    <!-- Item Not Found -->
    <div v-else class="not-found">
      <h3>Item Not Found</h3>
      <p>The item you're looking for doesn't exist or has been deleted.</p>
      <RouterLink to="/items" class="btn btn-primary">Back to Items</RouterLink>
    </div>

    <!-- Delete Confirmation Modal -->
    <div v-if="showDeleteModal" class="modal-overlay" @click="showDeleteModal = false">
      <div class="modal" @click.stop>
        <h3>Confirm Delete</h3>
        <p>Are you sure you want to delete "{{ item?.name }}"?</p>
        <div class="modal-actions">
          <button @click="showDeleteModal = false" class="btn btn-secondary">Cancel</button>
          <button @click="handleDelete" class="btn btn-danger" :disabled="itemsStore.loading">
            {{ itemsStore.loading ? 'Deleting...' : 'Delete' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref, computed } from 'vue'
import { useRouter, useRoute, RouterLink } from 'vue-router'
import { useItemsStore } from '@/stores/items'

const router = useRouter()
const route = useRoute()
const itemsStore = useItemsStore()

const showDeleteModal = ref(false)

const itemId = computed(() => parseInt(route.params.id as string))
const item = computed(() => itemsStore.getItemById(itemId.value))

onMounted(() => {
  loadItem()
})

async function loadItem() {
  if (!item.value) {
    await itemsStore.fetchItem(itemId.value)
  }
}

function formatDate(dateString: string): string {
  return new Date(dateString).toLocaleString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit'
  })
}

async function handleDelete() {
  if (item.value) {
    const success = await itemsStore.deleteItem(item.value.id)
    if (success) {
      router.push('/items')
    }
  }
}
</script>

<style scoped>
.item-detail-view {
  padding: 2rem;
  max-width: 800px;
  margin: 0 auto;
}

.header {
  margin-bottom: 2rem;
}

.breadcrumb {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  color: #7f8c8d;
}

.breadcrumb-link {
  color: #3498db;
  text-decoration: none;
}

.breadcrumb-link:hover {
  text-decoration: underline;
}

.breadcrumb-separator {
  color: #bdc3c7;
}

.breadcrumb-current {
  color: #2c3e50;
  font-weight: 500;
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

.error-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-top: 1rem;
}

.not-found {
  text-align: center;
  padding: 4rem;
  color: #7f8c8d;
}

.item-container {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.item-card {
  background: white;
  border: 1px solid #e1e8ed;
  border-radius: 0.75rem;
  overflow: hidden;
}

.item-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1rem;
  padding: 2rem 2rem 1rem;
  border-bottom: 1px solid #f8f9fa;
}

.item-header h1 {
  margin: 0;
  color: #2c3e50;
  flex: 1;
}

.item-actions {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.item-content {
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.field {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.field-label {
  font-weight: 600;
  color: #2c3e50;
  font-size: 0.875rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.field-value {
  color: #555;
  line-height: 1.5;
  padding: 0.75rem 1rem;
  background: #f8f9fa;
  border-radius: 0.5rem;
  border: 1px solid #e9ecef;
}

.no-value {
  color: #aaa;
  font-style: italic;
}

.back-link {
  display: flex;
  justify-content: flex-start;
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

.btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn-primary {
  background: #3498db;
  color: white;
}

.btn-primary:hover:not(:disabled) {
  background: #2980b9;
}

.btn-secondary {
  background: #95a5a6;
  color: white;
}

.btn-secondary:hover {
  background: #7f8c8d;
}

.btn-danger {
  background: #e74c3c;
  color: white;
}

.btn-danger:hover:not(:disabled) {
  background: #c0392b;
}

.icon {
  font-size: 1rem;
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
  .item-detail-view {
    padding: 1rem;
  }

  .item-header {
    flex-direction: column;
    gap: 1rem;
    align-items: stretch;
  }

  .item-actions {
    justify-content: flex-start;
  }

  .item-content {
    padding: 1rem;
  }

  .error-actions {
    flex-direction: column;
    align-items: center;
  }

  .modal-actions {
    flex-direction: column-reverse;
  }
}
</style>