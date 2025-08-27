<template>
  <div class="bg-white p-6 rounded-lg shadow">
    <h2 class="text-xl font-bold mb-4">Upload Flight Data</h2>
    <form @submit.prevent="upload" class="space-y-4">
      <div>
        <label class="block mb-1">Blackbox Log (.bfl)</label>
        <input type="file" accept=".bfl" @change="onLogChange" required class="border rounded px-3 py-2 w-full"/>
      </div>
      <div>
        <label class="block mb-1">FPV Video (optional)</label>
        <input type="file" accept="video/*" @change="onVideoChange" class="border rounded px-3 py-2 w-full"/>
      </div>
      <button type="submit" :disabled="uploading" class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 disabled:opacity-50">
        {{ uploading ? 'Uploading...' : 'Upload' }}
      </button>
    </form>
    <p v-if="message" class="mt-2 text-sm text-gray-600">{{ message }}</p>
  </div>
</template>

<script>
import api from '../services/api'

export default {
  data() {
    return {
      logFile: null,
      videoFile: null,
      uploading: false,
      message: ''
    }
  },
  methods: {
    onLogChange(e) {
      this.logFile = e.target.files[0]
    },
    onVideoChange(e) {
      this.videoFile = e.target.files[0]
    },
    async upload() {
      this.uploading = true
      this.message = 'Uploading...'
      try {
        const res = await api.uploadFlight(this.logFile, this.videoFile)
        this.message = `✅ Uploaded! Flight ID: ${res.data.flight_id}`
        this.$emit('uploaded', res.data)
      } catch (err) {
        this.message = '❌ Upload failed: ' + err.message
      } finally {
        this.uploading = false
      }
    }
  }
}
</script>