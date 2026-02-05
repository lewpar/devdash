<script setup lang="ts">
import { Knob, ProgressSpinner } from 'primevue';
import { ref, onMounted } from 'vue';

interface CPUUsageResponse {
    unit: string,
    min: number,
    max: number,
    current: number
}

const cpuUsage = ref<CPUUsageResponse | null>(null);

async function fetchStats() {
    cpuUsage.value = null;

    const result = await fetch("http://127.0.0.1:8000/system/cpu/usage");
    const usage = (await result.json()) as CPUUsageResponse;

    cpuUsage.value = usage;
}

onMounted(async () => {
    await fetchStats();

    setInterval(fetchStats, 2500);
})
</script>

<template>
    <div id="cpu-usage">
        <h4>CPU Usage</h4>
        <Knob v-if="cpuUsage" v-model="cpuUsage.current" :min="cpuUsage.min" :max="cpuUsage.max" value-template="{value}%" readonly/>
        <ProgressSpinner v-else/>
    </div>
</template>

<style scoped>
#cpu-usage {
    display: flex;
    flex-direction: column;

    align-items: center;
}
</style>