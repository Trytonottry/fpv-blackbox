<template>
  <div class="bg-white p-6 rounded-lg shadow">
    <h2 class="text-xl font-bold mb-4">Your Flights</h2>
    <div v-if="flights.length === 0" class="text-gray-500">No flights yet</div>
    <div v-else class="space-y-2">
      <div v-for="f in flights" :key="f.id" class="border p-3 rounded hover:bg-gray-50 cursor-pointer" @click="$emit('select', f)">
        <div class="font-medium">Flight #{{ f.id }}</div>
        <div class="text-sm text-gray-600">Duration: {{ f.duration.toFixed(1) }}s</div>
      </div>
    </div>
  </div>
</template>

<script>
import api from '../services/api'

export default {
  data() {
    return {
      flights: []
    }
  },
  async mounted() {
    const res = await api.getFlights()
    this.flights = res.data
  }
}
</script>