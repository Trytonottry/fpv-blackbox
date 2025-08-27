<template>
  <div>
    <canvas ref="chart"></canvas>
  </div>
</template>

<script>
import { Chart, registerables } from 'chart.js'
Chart.register(...registerables)

export default {
  props: ['data'],
  mounted() {
    this.renderChart()
  },
  methods: {
    renderChart() {
      const ctx = this.$refs.chart.getContext('2d')
      new Chart(ctx, {
        type: 'line',
        data: {
          labels: this.data.slice(0, 100).map((_, i) => i),
          datasets: [
            {
              label: 'Gyro X',
              data: this.data.slice(0, 100).map(p => p.gx),
              borderColor: 'rgb(255, 99, 132)'
            },
            {
              label: 'Accel Y',
              data: this.data.slice(0, 100).map(p => p.ay),
              borderColor: 'rgb(54, 162, 235)'
            }
          ]
        },
        options: { responsive: true, maintainAspectRatio: false }
      })
    }
  }
}
</script>