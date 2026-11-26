import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Served from https://aiwithrakshi-dev.github.io/aiwithrakshi-dev/
export default defineConfig({
  plugins: [react()],
  base: '/aiwithrakshi-dev/',
})
