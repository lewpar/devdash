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
            <div id="header">
                <h1 id="title">{{ route.meta.title }}</h1>
                <pre id="subtitle">{{ route.meta.description }}</pre>
            </div>

            <template v-if="route.meta.hideCard">
                <RouterView />
            </template>
            <Card v-else>
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

    display: flex;
    flex-direction: column;

    gap: 1rem;
    
    padding: 1rem;

    /* background-color: red; */
}

main #page #header #title {
    font-size: 1.25rem;
    margin: 0;
}
main #page #header #subtitle {
    font-size: 1rem;
    margin: 0;
    color: gray;
}
</style>
