import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

export interface Item {
  id: number
  name: string
  description?: string
  created_at: string
}

export interface ItemCreate {
  name: string
  description?: string
}

export interface ItemUpdate {
  name?: string
  description?: string
}

class ApiService {
  private api = axios.create({
    baseURL: `${API_BASE_URL}/api/v1`,
    headers: {
      'Content-Type': 'application/json'
    }
  })

  async getItems(): Promise<Item[]> {
    const response = await this.api.get<Item[]>('/items/')
    return response.data
  }

  async getItem(id: number): Promise<Item> {
    const response = await this.api.get<Item>(`/items/${id}`)
    return response.data
  }

  async createItem(item: ItemCreate): Promise<Item> {
    const response = await this.api.post<Item>('/items/', item)
    return response.data
  }

  async updateItem(id: number, item: ItemUpdate): Promise<Item> {
    const response = await this.api.put<Item>(`/items/${id}`, item)
    return response.data
  }

  async deleteItem(id: number): Promise<void> {
    await this.api.delete(`/items/${id}`)
  }
}

export const apiService = new ApiService()