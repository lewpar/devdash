<script setup lang="ts">
import { Divider, Card } from "primevue";
import { routes } from "@/router";
</script>

<template>
    <nav>
        <Card id="sidebar">
            <template #content>
                <h3>Developer Dashboard</h3>
                <Divider/>
                <ul class="sidebar-menu">
                    <li v-for="route in routes" class="sidebar-menu-item">
                        <RouterLink :to="route.path">
                            <component :is="route.meta.icon"/> {{ route.meta.navLabel }}
                        </RouterLink>
                    </li>
                </ul>
            </template>
        </Card>
    </nav>
</template>

<style scoped>
#sidebar {
    flex: 1;
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
    gap: 0.5rem;
}

.sidebar-menu-item a {
    display: flex;
    flex-direction: row;

    align-items: center;

    gap: 0.5rem;
    padding: 0.75rem;
    border-radius: 0.33rem;

    color: oklch(0.37 0.03 260.73 / 1);
    text-decoration: none;

    font-size: 1rem;
    font-weight: 500;
}
.sidebar-menu-item a:hover {
    background-color: oklch(98.5% .002 247.839);
}
.sidebar-menu-item a.router-link-active {
    color: white;
    background-color: rgb(99 182 134);
}
</style>