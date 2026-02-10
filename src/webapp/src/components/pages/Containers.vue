<script setup lang="ts">
import { Button, ProgressSpinner, Card, Dialog } from 'primevue';
import { ref, onMounted } from 'vue';

interface DockerContainers {
    id: string;
    name: string;
}

const containers = ref<DockerContainers[] | null | undefined>(undefined);
const visible = ref(false);

onMounted(async () => {
    const result = await fetch("http://localhost:8000/containers");
    const containersResult = (await result.json()) as DockerContainers[];

    containers.value = containersResult.length < 1 ? null : containersResult;
});

function openDialog() {
    visible.value = true;
}

function closeDialog() {
    visible.value = false;
}
</script>

<template>
    <div id="containers">
        <template v-if="containers">
            <Card v-for="container in containers">
                <template #title>
                    {{ container.name }}
                </template>
                <template #subtitle>
                    {{ container.id }}
                </template>

                <template #content>
                    <Button v-on:click="openDialog">Manage</Button>
                </template>
            </Card>
        </template>
        <template v-else>
            <template v-if="containers == undefined">
                <ProgressSpinner/>
            </template>
            <template v-else>
                <div>No containers created yet.</div>
            </template>
        </template>

        <Dialog v-model:visible="visible" modal header="Manage Container">
            <Button v-on:click="closeDialog">Close</Button>
        </Dialog>
    </div>
</template>

<style scoped>
#containers {
    display: flex;
    flex-direction: column;

    gap: 1rem;
}

h3 {
    margin: 0;
}
</style>