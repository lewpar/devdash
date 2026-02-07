<script setup lang="ts">
import { Knob, ProgressSpinner } from 'primevue';
import { ref, onMounted } from 'vue';

interface CPUUsage {
    unit: string,
    min: number,
    max: number,
    current: number
}

const props = defineProps<{
    usage: CPUUsage
}>();
</script>

<template>
    <div id="cpu-usage">
        <h4>CPU Usage</h4>
        <Knob v-if="usage" v-model="usage.current" :min="usage.min" :max="usage.max" value-template="{value}%" readonly/>
        <ProgressSpinner v-else/>
    </div>
</template>

<style scoped>
#cpu-usage {
    display: flex;
    flex-direction: column;

    align-self: start;
}

#cpu-usage h4 {
    margin: 0;
    margin-bottom: 0.5rem;
}
</style>