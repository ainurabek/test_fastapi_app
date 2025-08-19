<template>
  <div class="create-item-view">
    <header class="header">
      <div class="breadcrumb">
        <RouterLink to="/items" class="breadcrumb-link">Items</RouterLink>
        <span class="breadcrumb-separator">/</span>
        <span class="breadcrumb-current">Create New Item</span>
      </div>
    </header>

    <div class="form-container">
      <h1>Create New Item</h1>

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
          <RouterLink to="/items" class="btn btn-secondary">Cancel</RouterLink>
          <button
            type="submit"
            class="btn btn-primary"
            :disabled="itemsStore.loading || !isFormValid"
          >
            <span v-if="itemsStore.loading" class="spinner-sm"></span>
            {{ itemsStore.loading ? 'Creating...' : 'Create Item' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, computed } from 'vue'
import { useRouter, RouterLink } from 'vue-router'
import { useItemsStore } from '@/stores/items'

const router = useRouter()
const itemsStore = useItemsStore()

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
  if (!validateForm()) {
    return
  }

  const itemData = {
    name: form.name.trim(),
    description: form.description.trim() || undefined
  }

  const newItem = await itemsStore.createItem(itemData)
  
  if (newItem) {
    router.push('/items')
  }
}
</script>

<style scoped>
.create-item-view {
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

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@media (max-width: 768px) {
  .create-item-view {
    padding: 1rem;
  }

  .form-container {
    padding: 1rem;
  }

  .form-actions {
    flex-direction: column-reverse;
  }
}
</style>