import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { apiService, type Item, type ItemCreate, type ItemUpdate } from '@/services/api'

export const useItemsStore = defineStore('items', () => {
  const items = ref<Item[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)

  const sortedItems = computed(() => {
    return [...items.value].sort((a, b) => new Date(b.created_at).getTime() - new Date(a.created_at).getTime())
  })

  const getItemById = computed(() => {
    return (id: number) => items.value.find(item => item.id === id)
  })

  async function fetchItems() {
    loading.value = true
    error.value = null
    try {
      items.value = await apiService.getItems()
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Failed to fetch items'
      console.error('Error fetching items:', err)
    } finally {
      loading.value = false
    }
  }

  async function fetchItem(id: number): Promise<Item | null> {
    loading.value = true
    error.value = null
    try {
      const item = await apiService.getItem(id)
      // Update the item in the store if it exists
      const index = items.value.findIndex(i => i.id === id)
      if (index !== -1) {
        items.value[index] = item
      } else {
        items.value.push(item)
      }
      return item
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Failed to fetch item'
      console.error('Error fetching item:', err)
      return null
    } finally {
      loading.value = false
    }
  }

  async function createItem(itemData: ItemCreate): Promise<Item | null> {
    loading.value = true
    error.value = null
    try {
      const newItem = await apiService.createItem(itemData)
      items.value.unshift(newItem) // Add to beginning of array
      return newItem
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Failed to create item'
      console.error('Error creating item:', err)
      return null
    } finally {
      loading.value = false
    }
  }

  async function updateItem(id: number, itemData: ItemUpdate): Promise<Item | null> {
    loading.value = true
    error.value = null
    try {
      const updatedItem = await apiService.updateItem(id, itemData)
      const index = items.value.findIndex(item => item.id === id)
      if (index !== -1) {
        items.value[index] = updatedItem
      }
      return updatedItem
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Failed to update item'
      console.error('Error updating item:', err)
      return null
    } finally {
      loading.value = false
    }
  }

  async function deleteItem(id: number): Promise<boolean> {
    loading.value = true
    error.value = null
    try {
      await apiService.deleteItem(id)
      items.value = items.value.filter(item => item.id !== id)
      return true
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Failed to delete item'
      console.error('Error deleting item:', err)
      return false
    } finally {
      loading.value = false
    }
  }

  function clearError() {
    error.value = null
  }

  return {
    items,
    sortedItems,
    loading,
    error,
    getItemById,
    fetchItems,
    fetchItem,
    createItem,
    updateItem,
    deleteItem,
    clearError
  }
})