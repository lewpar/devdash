<script setup lang="ts">
import SidebarMenu from './components/SidebarMenu.vue';
</script>

<template>
    <main>
        <SidebarMenu/>
        <div id="page">
            <RouterView />
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
