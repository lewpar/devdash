import { createMemoryHistory, createRouter } from 'vue-router';

import Dashboard from './components/pages/Dashboard.vue';
import System from './components/pages/System.vue';
import Containers from './components/pages/Containers.vue';

import { PhMonitor, PhChartBarHorizontal, PhCube } from '@phosphor-icons/vue';

export const routes = [
  { 
    path: '/', 
    component: Dashboard, 
    meta: {
      title: "Dashboard",
      navLabel: "Dashboard",
      description: "Overview of your local system",
      icon: PhMonitor
    } 
  },
  {
    path: '/system',
    component: System,
    meta: {
      title: "System Resources",
      navLabel: "System",
      description: "Monitor CPU, memory, and disk usage in real-time",
      icon: PhChartBarHorizontal
    }
  },
  {
    path: '/containers',
    component: Containers,
    meta: {
      title: "Docker Containers",
      navLabel: "Containers",
      description: "Manage your docker containers",
      icon: PhCube,
      hideCard: true
    }
  }
];

const router = createRouter({
  history: createMemoryHistory(),
  routes,
});

export default router;