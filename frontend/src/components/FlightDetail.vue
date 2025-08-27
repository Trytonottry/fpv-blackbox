<template>
  <div class="bg-white p-6 rounded-lg shadow">
    <h2 class="text-xl font-bold mb-4">Flight #{{ flight.id }}</h2>
    <div class="space-y-4">
      <TelemetryChart :data="telemetry" />
      <Flight3DViewer :data="telemetry" />
      <div v-if="analysis">
        <h3 class="font-bold">AI Analysis</h3>
        <p>Risk: {{ (analysis.risk * 100).toFixed(1) }}%</p>
        <p>{{ analysis.advice }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import TelemetryChart from './TelemetryChart.vue'
import Flight3DViewer from './Flight3DViewer.vue'
import api from '../services/api'

export default {
  components: { TelemetryChart, Flight3DViewer },
  props: ['flight'],
  data() {
    return {
      telemetry: [],
      analysis: null
    }
  },
  async mounted() {
    const res = await api.getFlight(this.flight.id)
    this.telemetry = res.data.telemetry
    const ana = await api.analyzeFlight(this.flight.id)
    this.analysis = ana.data
  }
}
</script>