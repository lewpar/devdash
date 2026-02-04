<script setup lang="ts">
import { Card } from 'primevue';
import CPUUsage from '../system/CPUUsage.vue';
</script>

<template>
    <div id="dashboard">
        <h2>Dashboard</h2>

        <Card>
            <template #content>
                <CPUUsage/>
            </template>
        </Card>
    </div>
</template>

<style scoped>
#dashboard {
    display: flex;
    flex-direction: column;
}
</style>