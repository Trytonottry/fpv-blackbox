<template>
  <div>
    <canvas ref="canvas" class="w-full h-80"></canvas>
  </div>
</template>

<script>
import * as THREE from 'three'

export default {
  props: ['data'],
  mounted() {
    this.init3D()
  },
  methods: {
    init3D() {
      const canvas = this.$refs.canvas
      const renderer = new THREE.WebGLRenderer({ canvas, antialias: true })
      const scene = new THREE.Scene()
      const camera = new THREE.PerspectiveCamera(75, canvas.clientWidth / canvas.clientHeight, 0.1, 1000)
      camera.position.z = 5

      const points = this.data.slice(0, 200).map(p => new THREE.Vector3(p.gx / 100, p.gy / 100, p.gz / 100))
      const geometry = new THREE.BufferGeometry().setFromPoints(points)
      const material = new THREE.LineBasicMaterial({ color: 0x00ff00 })
      const line = new THREE.Line(geometry, material)
      scene.add(line)

      const animate = () => {
        requestAnimationFrame(animate)
        line.rotation.x += 0.005
        line.rotation.y += 0.005
        renderer.render(scene, camera)
      }
      animate()

      window.addEventListener('resize', () => {
        camera.aspect = canvas.clientWidth / canvas.clientHeight
        camera.updateProjectionMatrix()
        renderer.setSize(canvas.clientWidth, canvas.clientHeight)
      })
    }
  }
}
</script>