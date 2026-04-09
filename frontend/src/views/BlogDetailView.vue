<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { api } from '@/api/index.js'
import AppFooter from '@/components/AppFooter.vue'

const route = useRoute()
const post = ref(null)
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    post.value = await api.post(route.params.slug)
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
        <p>Post no encontrado.</p>
        <router-link to="/" class="btn btn-outline">Volver</router-link>
      </div>

      <article v-else class="detail-article">
        <time v-if="post.created_at">{{ new Date(post.created_at).toLocaleDateString('es-ES', { day: 'numeric', month: 'long', year: 'numeric' }) }}</time>
        <h1>{{ post.title }}</h1>
        <p class="detail-excerpt">{{ post.excerpt }}</p>
        <img v-if="post.image" :src="post.image" :alt="post.title" class="detail-hero-img" loading="eager" />
        <div class="detail-body" v-html="post.content"></div>
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
  max-width: 750px;
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

.detail-article time {
  font-size: 0.85rem;
  color: var(--color-text-muted);
  text-transform: uppercase;
  letter-spacing: 0.03em;
}

.detail-article h1 {
  font-size: 2.25rem;
  margin: 0.5rem 0 1rem;
}

.detail-excerpt {
  font-size: 1.15rem;
  color: var(--color-text-muted);
  line-height: 1.6;
  margin-bottom: 2rem;
}

.detail-hero-img {
  width: 100%;
  border-radius: var(--radius-lg);
  margin-bottom: 2rem;
}

.detail-body {
  font-size: 1.05rem;
  line-height: 1.85;
  color: var(--color-text);
}
.detail-body :deep(h2) { font-size: 1.5rem; margin: 2rem 0 1rem; }
.detail-body :deep(h3) { font-size: 1.25rem; margin: 1.5rem 0 0.75rem; }
.detail-body :deep(p) { margin-bottom: 1.25rem; }
.detail-body :deep(ul), .detail-body :deep(ol) { padding-left: 1.5rem; margin-bottom: 1.25rem; list-style: revert; }
.detail-body :deep(a) { color: var(--color-accent); text-decoration: underline; }
.detail-body :deep(img) { border-radius: var(--radius-md); margin: 1.5rem 0; }
.detail-body :deep(pre) {
  background: var(--c-gray-900);
  color: var(--c-gray-100);
  padding: 1rem;
  border-radius: var(--radius-md);
  overflow-x: auto;
  margin-bottom: 1.25rem;
  font-family: var(--font-mono);
  font-size: 0.9rem;
}
.detail-body :deep(code) {
  font-family: var(--font-mono);
  font-size: 0.9em;
  background: var(--c-gray-100);
  padding: 0.15rem 0.35rem;
  border-radius: var(--radius-sm);
}
.detail-body :deep(pre code) { background: none; padding: 0; }
.detail-body :deep(blockquote) {
  border-left: 3px solid var(--color-accent);
  padding-left: 1rem;
  color: var(--color-text-muted);
  margin: 1.5rem 0;
  font-style: italic;
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
