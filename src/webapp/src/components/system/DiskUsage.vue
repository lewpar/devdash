<script setup lang="ts">
import { MeterGroup, type MeterItem } from 'primevue';

const props = defineProps<{
    usage: MeterItem[],
    max: number
}>();
</script>

<template>
    <div id="disk-usage">
        <h4>Disk Usage</h4>
        <MeterGroup :value="props.usage" :max="props.max" />
    </div>
</template>

<style scoped>
#disk-usage {
    display: flex;
    flex-direction: column;
}
</style>