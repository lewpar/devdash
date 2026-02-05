<script setup lang="ts">
import CPUUsage from '../system/CPUUsage.vue';
</script>

<template>
    <div id="dashboard">
        <CPUUsage/>
    </div>
</template>

<style scoped>
#dashboard {
    display: flex;
    flex-direction: column;
}
</style>