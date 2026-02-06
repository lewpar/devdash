<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { ProgressSpinner } from 'primevue';
import CPUUsage from '../system/CPUUsage.vue';

interface CPUInfo {
    frequency: {
        unit: number,
        min: number,
        max: number,
        current: number
    },
    usage: {
        unit: string,
        min: number,
        max: number,
        current: number
    },
    cores: {
        count: number
    }
}

const cpuInfo = ref<CPUInfo | null>(null);

async function getCPUInfo() {
    const result = await fetch("http://localhost:8000/system/cpu");
    const info = (await result.json()) as CPUInfo;

    cpuInfo.value = info;
}

onMounted(async () => {
    await getCPUInfo();

    setInterval(getCPUInfo, 2500);
});
</script>

<template>
    <div v-if="cpuInfo">
        <CPUUsage :usage="cpuInfo.usage"/>
    </div>
    <ProgressSpinner v-else/>
</template>