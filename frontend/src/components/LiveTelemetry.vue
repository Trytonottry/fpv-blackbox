<template>
  <div class="bg-gray-100 p-4 rounded">
    <h3>Live Telemetry</h3>
    <div v-for="(val, key) in data" :key="key">
      {{ key }}: {{ val }}
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      data: {}
    }
  },
  mounted() {
    const ws = new WebSocket("ws://localhost:8000/api/ws/live")
    ws.onmessage = (e) => {
      this.data = JSON.parse(e.data)
    }
  }
}
</script>