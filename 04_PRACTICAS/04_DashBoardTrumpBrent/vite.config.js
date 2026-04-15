import { defineConfig } from 'vite';

export default defineConfig({
  // Base configuration
  root: './',
  base: './', // Ensures assets are relative to index.html
  build: {
    outDir: 'dist',
    minify: 'terser',
    sourcemap: false,
    emptyOutDir: true,
    rollupOptions: {
      input: {
        main: './index.html',
      },
    },
  },
  server: {
    port: 8000,
    open: true,
  },
});
