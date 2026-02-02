<script setup lang="ts">
</script>

<template>
    <ul class="sidebar-menu">
        <li class="sidebar-menu-item">
            <RouterLink to="/">Dashboard</RouterLink>
        </li>
    </ul>
</template>

<style scoped>
.sidebar-menu {
    display: flex;
    flex-direction: column;

    list-style: none;
    padding-inline-start: 0;
    margin: 0;
}

.sidebar-menu-item {

}
</style>