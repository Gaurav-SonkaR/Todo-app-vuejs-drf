import { createMemoryHistory, createRouter } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import AddView from '../views/AddView.vue'
import UpdateView from '../views/UpdateView.vue'

const routes = [
  { path: '/',  component: HomeView, name: 'home' },
  { path: '/add', component: AddView, name : 'add' },
  { path: '/update/:id', component: UpdateView , name : 'update',props: true},
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

export default router