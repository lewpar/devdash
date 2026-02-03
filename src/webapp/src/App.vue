<script setup lang="ts">
import SidebarMenu from './components/SidebarMenu.vue';
</script>

<template>
    <main>
        <SidebarMenu/>
        <RouterView />
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
</style>
