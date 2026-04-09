<script setup>
import { ref, onMounted, nextTick } from 'vue'
import { api } from '@/api/index.js'
import AppFooter from '@/components/AppFooter.vue'

const posts = ref([])
const about = ref(null)
const loading = ref(true)
const error = ref(null)
const ready = ref(false)

onMounted(async () => {
  try {
    const [homeData, aboutData] = await Promise.all([
      api.home(),
      api.about(),
    ])
    posts.value = homeData.recent_posts || []
    about.value = aboutData.about || null
  } catch (e) {
    error.value = e
  } finally {
    loading.value = false
    await nextTick()
    requestAnimationFrame(() => { ready.value = true })
  }
})
</script>

<template>
  <main style="padding-top: var(--nav-height)">
    <div v-if="loading" class="loading-screen">
      <div class="spinner"></div>
      <p>Cargando…</p>
    </div>

    <div v-else-if="error" class="loading-screen">
      <p style="color: #b91c1c">Error al cargar los datos.</p>
    </div>

    <template v-else>
      <div class="page-enter" :class="{ ready }">
        <section class="section">
          <div class="container">
            <h1 class="section-title page-anim page-stagger-1">Blog</h1>
            <p class="section-subtitle page-anim page-stagger-2">Artículos y reflexiones</p>

            <div v-if="posts.length" class="blog-grid page-anim page-stagger-3">
            <router-link
              v-for="post in posts"
              :key="post.id"
              :to="`/blog/${post.slug}`"
              class="card blog-card"
            >
              <div class="blog-img" v-if="post.image">
                <img :src="post.image" :alt="post.title" loading="lazy" />
              </div>
              <div class="blog-body">
                <time v-if="post.created_at">{{ new Date(post.created_at).toLocaleDateString('es-ES', { day: 'numeric', month: 'long', year: 'numeric' }) }}</time>
                <h3>{{ post.title }}</h3>
                <p>{{ post.excerpt }}</p>
              </div>
            </router-link>
          </div>
          <p v-else class="empty-msg page-anim page-stagger-3">No hay artículos todavía.</p>
          </div>
        </section>
        <div class="page-anim page-stagger-4">
          <AppFooter :about="about" />
        </div>
      </div>
    </template>
  </main>
</template>

<style scoped>
.loading-screen {
  min-height: calc(100vh - var(--nav-height));
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  color: var(--color-text-muted);
}

.spinner {
  width: 36px;
  height: 36px;
  border: 3px solid var(--c-gray-200);
  border-top-color: var(--color-accent);
  border-radius: 50%;
  animation: spin 0.7s linear infinite;
}
@keyframes spin {
  to { transform: rotate(360deg); }
}

.blog-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.5rem;
}

.blog-card {
  display: flex;
  flex-direction: column;
  color: inherit;
}

.blog-img {
  aspect-ratio: 16 / 9;
  overflow: hidden;
  background: var(--c-gray-100);
}
.blog-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s;
}
.blog-card:hover .blog-img img {
  transform: scale(1.04);
}

.blog-body {
  padding: 1.25rem;
  flex: 1;
}
.blog-body time {
  font-size: 0.8rem;
  color: var(--color-text-muted);
  text-transform: uppercase;
  letter-spacing: 0.03em;
}
.blog-body h3 {
  font-size: 1.1rem;
  margin: 0.4rem 0 0.5rem;
}
.blog-body p {
  color: var(--color-text-muted);
  font-size: 0.9rem;
  line-height: 1.6;
}

.empty-msg {
  text-align: center;
  color: var(--color-text-muted);
  padding: 3rem 0;
}
</style>
