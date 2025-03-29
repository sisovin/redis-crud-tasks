import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/pages/Home.vue';
import Dashboard from '@/pages/Dashboard.vue';
import Tasks from '@/pages/Tasks.vue';
import Login from '@/components/auth/Login.vue';
import Register from '@/components/auth/Register.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
  },
  {
    path: '/tasks',
    name: 'Tasks',
    component: Tasks,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
