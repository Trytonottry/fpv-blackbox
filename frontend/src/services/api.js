import axios from 'axios'

const API = axios.create({
  baseURL: '/api',
  timeout: 10000
})

export default {
  async uploadFlight(logFile, videoFile) {
    const formData = new FormData()
    formData.append('log_file', logFile)
    if (videoFile) formData.append('video_file', videoFile)
    return API.post('/upload', formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    })
  },

  async getFlights() {
    return API.get('/flights')
  },

  async getFlight(id) {
    return API.get(`/flights/${id}`)
  },

  async analyzeFlight(id) {
    return API.get(`/analyze/${id}`)
  }
}