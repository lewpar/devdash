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
    display: flex;
    flex-direction: row;
}
</style>
