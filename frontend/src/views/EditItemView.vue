<template>
  <div class="edit-item-view">
    <header class="header">
      <div class="breadcrumb">
        <RouterLink to="/items" class="breadcrumb-link">Items</RouterLink>
        <span class="breadcrumb-separator">/</span>
        <RouterLink v-if="item" :to="`/items/${item.id}`" class="breadcrumb-link">{{ item.name }}</RouterLink>
        <span class="breadcrumb-separator">/</span>
        <span class="breadcrumb-current">Edit</span>
      </div>
    </header>

    <!-- Loading State -->
    <div v-if="itemsStore.loading && !item" class="loading">
      <div class="spinner"></div>
      <p>Loading item...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="itemsStore.error && !item" class="error">
      <h3>Error</h3>
      <p>{{ itemsStore.error }}</p>
      <div class="error-actions">
        <button @click="loadItem" class="btn btn-secondary">Try Again</button>
        <RouterLink to="/items" class="btn btn-primary">Back to Items</RouterLink>
      </div>
    </div>

    <!-- Item Not Found -->
    <div v-else-if="!item && !itemsStore.loading" class="not-found">
      <h3>Item Not Found</h3>
      <p>The item you're trying to edit doesn't exist or has been deleted.</p>
      <RouterLink to="/items" class="btn btn-primary">Back to Items</RouterLink>
    </div>

    <!-- Edit Form -->
    <div v-else-if="item" class="form-container">
      <h1>Edit Item</h1>

      <!-- Error Display -->
      <div v-if="itemsStore.error" class="error-message">
        <p>{{ itemsStore.error }}</p>
        <button @click="itemsStore.clearError" class="btn btn-sm btn-secondary">Dismiss</button>
      </div>

      <form @submit.prevent="handleSubmit" class="item-form">
        <div class="form-group">
          <label for="name" class="form-label">Name *</label>
          <input
            id="name"
            v-model="form.name"
            type="text"
            class="form-input"
            :class="{ 'form-input-error': errors.name }"
            placeholder="Enter item name"
            required
          />
          <span v-if="errors.name" class="error-text">{{ errors.name }}</span>
        </div>

        <div class="form-group">
          <label for="description" class="form-label">Description</label>
          <textarea
            id="description"
            v-model="form.description"
            class="form-textarea"
            :class="{ 'form-input-error': errors.description }"
            placeholder="Enter item description (optional)"
            rows="4"
          ></textarea>
          <span v-if="errors.description" class="error-text">{{ errors.description }}</span>
        </div>

        <div class="form-actions">
          <RouterLink :to="`/items/${item.id}`" class="btn btn-secondary">Cancel</RouterLink>
          <button
            type="submit"
            class="btn btn-primary"
            :disabled="itemsStore.loading || !isFormValid || !hasChanges"
          >
            <span v-if="itemsStore.loading" class="spinner-sm"></span>
            {{ itemsStore.loading ? 'Saving...' : 'Save Changes' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, reactive, computed, watch } from 'vue'
import { useRouter, useRoute, RouterLink } from 'vue-router'
import { useItemsStore } from '@/stores/items'

const router = useRouter()
const route = useRoute()
const itemsStore = useItemsStore()

const itemId = computed(() => parseInt(route.params.id as string))
const item = computed(() => itemsStore.getItemById(itemId.value))

const form = reactive({
  name: '',
  description: ''
})

const errors = reactive({
  name: '',
  description: ''
})

const isFormValid = computed(() => {
  return form.name.trim().length > 0 && !errors.name && !errors.description
})

const hasChanges = computed(() => {
  if (!item.value) return false
  
  return (
    form.name.trim() !== item.value.name ||
    form.description !== (item.value.description || '')
  )
})

// Watch for item changes and update form
watch(item, (newItem) => {
  if (newItem) {
    form.name = newItem.name
    form.description = newItem.description || ''
  }
}, { immediate: true })

onMounted(() => {
  loadItem()
})

async function loadItem() {
  if (!item.value) {
    await itemsStore.fetchItem(itemId.value)
  }
}

function validateForm() {
  errors.name = ''
  errors.description = ''

  if (!form.name.trim()) {
    errors.name = 'Name is required'
  } else if (form.name.length > 255) {
    errors.name = 'Name must be less than 255 characters'
  }

  if (form.description && form.description.length > 1000) {
    errors.description = 'Description must be less than 1000 characters'
  }

  return !errors.name && !errors.description
}

async function handleSubmit() {
  if (!validateForm() || !item.value) {
    return
  }

  const updateData: { name?: string; description?: string } = {}
  
  if (form.name.trim() !== item.value.name) {
    updateData.name = form.name.trim()
  }
  
  if (form.description !== (item.value.description || '')) {
    updateData.description = form.description.trim() || undefined
  }

  if (Object.keys(updateData).length === 0) {
    // No changes to save
    router.push(`/items/${item.value.id}`)
    return
  }

  const updatedItem = await itemsStore.updateItem(item.value.id, updateData)
  
  if (updatedItem) {
    router.push(`/items/${updatedItem.id}`)
  }
}
</script>

<style scoped>
.edit-item-view {
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

.form-container {
  background: white;
  padding: 2rem;
  border-radius: 0.75rem;
  border: 1px solid #e1e8ed;
}

.form-container h1 {
  margin: 0 0 2rem;
  color: #2c3e50;
}

.error-message {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #fff5f5;
  color: #e74c3c;
  padding: 1rem;
  border-radius: 0.5rem;
  border: 1px solid #fecaca;
  margin-bottom: 2rem;
}

.error-message p {
  margin: 0;
}

.item-form {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-label {
  font-weight: 500;
  color: #2c3e50;
}

.form-input,
.form-textarea {
  padding: 0.75rem;
  border: 1px solid #d1d5db;
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.form-input:focus,
.form-textarea:focus {
  outline: none;
  border-color: #3498db;
  box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
}

.form-input-error {
  border-color: #e74c3c;
}

.form-input-error:focus {
  border-color: #e74c3c;
  box-shadow: 0 0 0 3px rgba(231, 76, 60, 0.1);
}

.form-textarea {
  resize: vertical;
  min-height: 100px;
}

.error-text {
  color: #e74c3c;
  font-size: 0.875rem;
}

.form-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
  padding-top: 1rem;
  border-top: 1px solid #f1f1f1;
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

.btn-sm {
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
}

.spinner-sm {
  width: 16px;
  height: 16px;
  border: 2px solid transparent;
  border-top: 2px solid currentColor;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@media (max-width: 768px) {
  .edit-item-view {
    padding: 1rem;
  }

  .form-container {
    padding: 1rem;
  }

  .form-actions {
    flex-direction: column-reverse;
  }

  .error-actions {
    flex-direction: column;
    align-items: center;
  }
}
</style>