<script setup lang="ts">
import { MeterGroup, type MeterItem } from 'primevue';

const props = defineProps<{
    usage: MeterItem[],
    max: number
}>();

function bytesToGigabytes(bytes: number) {
    return bytes / 1024 / 1024 / 1024;
}
</script>

<template>
    <div id="disk-usage">
        <MeterGroup id="disk-meter" :value="props.usage" :max="props.max">
            <template #start>
                <div id="disk-meter-range-labels">
                    <h4>Disk Usage</h4>
                    <div>{{ bytesToGigabytes(props.max).toLocaleString() }} GB</div>
                </div>
            </template>
        </MeterGroup>
    </div>
</template>

<style scoped>
#disk-usage {
    display: flex;
    flex-direction: column;
}

#disk-meter-range-labels {
    display: flex;
    flex-direction: row;

    justify-content: space-between;
}
#disk-meter-range-labels h4 {
    margin: 0;
}
</style>