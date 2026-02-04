<script setup lang="ts">
import { PhChartBarHorizontal } from "@phosphor-icons/vue";
import { Divider, Card } from "primevue";
</script>

<template>
    <nav>
        <Card id="sidebar">
            <template #content>
                <h3>DevDash</h3>
                <Divider/>
                <ul class="sidebar-menu">
                    <li class="sidebar-menu-item">
                        <RouterLink to="/"><PhChartBarHorizontal :size="20" /> Dashboard</RouterLink>
                    </li>
                </ul>
            </template>
        </Card>
    </nav>
</template>

<style scoped>
#sidebar {
    margin: 1rem;
    height: 100%;
}
#sidebar h3 {
    text-align: center;
}
nav {
    display: flex;
    flex-direction: column;
}
.sidebar-menu {
    flex: 1;

    display: flex;
    flex-direction: column;

    list-style: none;
    padding-inline-start: 0;

    margin: 0;
}

.sidebar-menu-item a {
    display: flex;
    flex-direction: row;

    align-items: center;

    gap: 0.5rem;
    padding: 0.5rem;
    border-radius: 0.625;

    color: oklch(0.37 0.03 260.73 / 1);
    text-decoration: none;

    font-size: 0.8rem;
}
.sidebar-menu-item a:hover {
    background-color: oklch(98.5% .002 247.839);
}
</style>