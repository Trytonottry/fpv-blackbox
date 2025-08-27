<template>
  <div>
    <h2>Flight Trajectory</h2>
    <canvas ref="canvas" width="800" height="600"></canvas>
  </div>
</template>

<script>
import { onMounted, ref } from 'vue'
import * as api from '../services/api'

export default {
  setup() {
    const canvas = ref(null)

    onMounted(async () => {
      const ctx = canvas.value.getContext('2d')
      const data = await api.getFlightTrajectory()
      // Простая 2D визуализация
      data.forEach((point, i) => {
        if (i === 0) return
        const prev = data[i-1]
        ctx.beginPath()
        ctx.moveTo(prev.x, prev.y)
        ctx.lineTo(point.x, point.y)
        ctx.stroke()
      })
    })

    return { canvas }
  }
}
</script>