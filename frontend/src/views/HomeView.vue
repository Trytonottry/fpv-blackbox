<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-6">FPV Blackbox Analyzer</h1>
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <UploadForm @uploaded="onUploaded" />
      <FlightList @select="onSelectFlight" />
      <div v-if="selectedFlight">
        <FlightDetail :flight="selectedFlight" />
      </div>
    </div>
  </div>
</template>

<script>
import UploadForm from '../components/UploadForm.vue'
import FlightList from '../components/FlightList.vue'
import FlightDetail from '../components/FlightDetail.vue'

export default {
  components: { UploadForm, FlightList, FlightDetail },
  data() {
    return {
      selectedFlight: null
    }
  },
  methods: {
    onUploaded(data) {
      // Обновляем список
    },
    onSelectFlight(flight) {
      this.selectedFlight = flight
    }
  }
}
</script>