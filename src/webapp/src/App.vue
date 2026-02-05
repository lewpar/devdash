<script setup lang="ts">
import { Card } from 'primevue';
import SidebarMenu from './components/SidebarMenu.vue';
import { useRoute } from 'vue-router';

const route = useRoute();
</script>

<template>
    <main>
        <SidebarMenu id="sidebar"/>
        <div id="page">
            <h2>{{ route.meta.title }}</h2>
            <Card>
                <template #content>
                    <RouterView />
                </template>
            </Card>
        </div>
    </main>
</template>

<style scoped>
main {
    flex: 1;

    display: flex;
    flex-direction: row;
}

main #sidebar {
    flex: 2;
    padding: 1rem;

    /* background-color: blue; */
}
main #page {
    flex: 8;
    padding: 1rem;

    /* background-color: red; */
}
</style>
