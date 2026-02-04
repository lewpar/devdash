<script setup lang="ts">
import Card from 'primevue/card';
import Knob from 'primevue/knob';
import { ref } from 'vue';


const value = ref(10);
</script>

<template>
    <div id="dashboard">
        <h2>Dashboard</h2>

        <Card>
            <template #content>
                <Knob v-model="value" value-template="{value}%" readonly/>
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