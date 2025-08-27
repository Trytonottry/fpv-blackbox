<template>
  <div class="font-sans text-gray-900">
    <header class="bg-blue-600 text-white p-4">
      <h1 class="text-xl">FPV Blackbox Analyzer</h1>
    </header>
    <main class="container mx-auto mt-6 px-4">
      <HomeView />
    </main>
  </div>
</template>

<script>
import HomeView from './views/HomeView.vue'

export default {
  components: { HomeView }
}
</script>