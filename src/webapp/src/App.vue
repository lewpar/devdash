<script setup>
import SidebarMenu from './components/SidebarMenu.vue'
import PageContent from './components/PageContent.vue'
</script>

<template>
  <main>
    <SidebarMenu/>
    <PageContent/>
  </main>
</template>

<style scoped>
main {
  display: flex;
  flex-direction: row;
}
</style>
