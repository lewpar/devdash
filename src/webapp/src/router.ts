import { createMemoryHistory, createRouter } from 'vue-router';
import Dashboard from './components/pages/Dashboard.vue';

const routes = [
  { path: '/', component: Dashboard }
];

const router = createRouter({
  history: createMemoryHistory(),
  routes,
});

export default router;