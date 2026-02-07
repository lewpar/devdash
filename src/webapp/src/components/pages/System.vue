<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { ProgressSpinner, type MeterItem } from 'primevue';
import CPUUsage from '../system/CPUUsage.vue';
import DiskUsage from '../system/DiskUsage.vue';

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

interface DiskUsage {
    unit: string;
    free: number;
    used: number;
    total: number;
}

const cpuInfo = ref<CPUInfo | null>(null);
const diskUsage = ref<MeterItem[] | null>(null);
const diskMax = ref<number>(100);

async function getSystemResources() {
    await getCPUInfo();
    await getDiskUsage();
}

async function getCPUInfo() {
    const result = await fetch("http://localhost:8000/system/cpu");
    const info = (await result.json()) as CPUInfo;

    cpuInfo.value = info;
}

async function getDiskUsage() {
    const result = await fetch("http://localhost:8000/system/disk/usage");
    const usage = (await result.json()) as DiskUsage;

    diskUsage.value = [
        {
            label: "Used",
            value: usage.used,
            color: "rgb(99 182 134)"
        },
        {
            label: "Free",
            value: usage.free,
            color: "#e4e8ef"
        }
    ];

    diskMax.value = usage.total;
}

onMounted(async () => {
    await getCPUInfo();
    await getDiskUsage();

    setInterval(getSystemResources, 2500);
});
</script>

<template>
    <div id="page-elements">
        <template v-if="cpuInfo">
            <CPUUsage :usage="cpuInfo.usage"/>
        </template>
        <ProgressSpinner v-else/>

        <template v-if="diskUsage">
            <DiskUsage :usage="diskUsage" :max="diskMax"/>
        </template>
        <ProgressSpinner v-else/>
    </div>
</template>

<style scoped>
#page-elements {
    display: flex;
    flex-direction: row;

    align-items: center;
    justify-content: center;

    flex-wrap: wrap;

    gap: 2rem;
}
</style>