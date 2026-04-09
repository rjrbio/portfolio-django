<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { api } from '@/api/index.js'
import AppFooter from '@/components/AppFooter.vue'

const route = useRoute()
const project = ref(null)
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    project.value = await api.project(route.params.slug)
  } catch (e) {
    error.value = e
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <main class="detail-page" style="padding-top: var(--nav-height)">
    <div class="container detail-container">
      <router-link to="/" class="back-link">← Volver al inicio</router-link>

      <div v-if="loading" class="detail-loading">
        <div class="spinner"></div>
      </div>
      <div v-else-if="error" class="detail-loading">
        <p>Proyecto no encontrado.</p>
        <router-link to="/" class="btn btn-outline">Volver</router-link>
      </div>

      <article v-else class="detail-article">
        <h1>{{ project.title }}</h1>
        <div class="detail-tags">
          <span class="badge" v-for="tech in project.technologies" :key="tech">{{ tech }}</span>
        </div>
        <img v-if="project.image" :src="project.image" :alt="project.title" class="detail-hero-img" />
        <div class="detail-body">
          <p>{{ project.description }}</p>
        </div>
        <div class="detail-actions">
          <a v-if="project.url" :href="project.url" target="_blank" rel="noopener" class="btn btn-primary">Ver proyecto</a>
          <a v-if="project.github_url" :href="project.github_url" target="_blank" rel="noopener" class="btn btn-outline">GitHub</a>
        </div>
      </article>
    </div>
    <AppFooter />
  </main>
</template>

<style scoped>
.detail-page { min-height: 100vh; }

.detail-container {
  padding-top: 2rem;
  padding-bottom: 4rem;
  max-width: 800px;
}

.back-link {
  display: inline-block;
  font-size: 0.9rem;
  color: var(--color-text-muted);
  margin-bottom: 2rem;
  transition: color 0.2s;
}
.back-link:hover { color: var(--color-accent); }

.detail-loading {
  text-align: center;
  padding: 4rem 0;
  color: var(--color-text-muted);
}

.detail-article h1 {
  font-size: 2.25rem;
  margin-bottom: 1rem;
}

.detail-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-bottom: 2rem;
}

.detail-hero-img {
  width: 100%;
  border-radius: var(--radius-lg);
  margin-bottom: 2rem;
}

.detail-body {
  font-size: 1.05rem;
  line-height: 1.8;
  color: var(--color-text);
  margin-bottom: 2rem;
}

.detail-actions {
  display: flex;
  gap: 1rem;
}

.spinner {
  width: 36px;
  height: 36px;
  border: 3px solid var(--c-gray-200);
  border-top-color: var(--color-accent);
  border-radius: 50%;
  animation: spin 0.7s linear infinite;
  margin: 0 auto;
}
@keyframes spin { to { transform: rotate(360deg); } }
</style>
