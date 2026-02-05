<script setup lang="ts">
import { Card } from 'primevue';
import SidebarMenu from './components/SidebarMenu.vue';
import { useRoute } from 'vue-router';

const route = useRoute();
</script>

<template>
    <main>
        <SidebarMenu/>
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

main:first-child {
    flex: 1;
}
main:last-child {
    flex: 2;
}

#page {
    flex: 1;

    padding: 1rem;
}
</style>
