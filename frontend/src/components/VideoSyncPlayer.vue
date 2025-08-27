<template>
  <div>
    <video v-if="videoUrl" ref="video" controls class="w-full" @timeupdate="onTimeUpdate">
      <source :src="videoUrl" type="video/mp4">
    </video>
    <div class="mt-2 text-sm text-gray-600">
      Time: {{ currentTime }}s | Telemetry: {{ telemetryTime }}s
    </div>
  </div>
</template>

<script>
export default {
  props: ['videoUrl', 'telemetry'],
  data() {
    return {
      currentTime: 0,
      telemetryTime: 0
    }
  },
  methods: {
    onTimeUpdate() {
      this.currentTime = this.$refs.video.currentTime
      // Здесь можно синхронизировать с телеметрией
    }
  }
}
</script>