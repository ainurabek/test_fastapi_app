import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/items',
      name: 'items',
      component: () => import('../views/ItemsView.vue'),
    },
    {
      path: '/items/create',
      name: 'create-item',
      component: () => import('../views/CreateItemView.vue'),
    },
    {
      path: '/items/:id',
      name: 'item-detail',
      component: () => import('../views/ItemDetailView.vue'),
      props: true
    },
    {
      path: '/items/:id/edit',
      name: 'edit-item',
      component: () => import('../views/EditItemView.vue'),
      props: true
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue'),
    },
  ],
})

export default router
