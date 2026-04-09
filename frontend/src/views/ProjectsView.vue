<script setup>
import { ref, onMounted, nextTick } from 'vue'
import { api } from '@/api/index.js'
import AppFooter from '@/components/AppFooter.vue'

const projects = ref([])
const about = ref(null)
const loading = ref(true)
const error = ref(null)
const ready = ref(false)

onMounted(async () => {
  try {
    const [projectsData, aboutData] = await Promise.all([
      api.projects(),
      api.about(),
    ])
    projects.value = projectsData
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
            <h1 class="section-title page-anim page-stagger-1">Proyectos</h1>
            <p class="section-subtitle page-anim page-stagger-2">Todo lo que he construido</p>

            <div v-if="projects.length" class="projects-grid page-anim page-stagger-3">
              <router-link
                v-for="project in projects"
                :key="project.id"
                :to="`/projects/${project.slug}`"
                class="card project-card"
              >
                <div class="project-img" v-if="project.image">
                  <img :src="project.image" :alt="project.title" loading="lazy" />
                </div>
                <div class="project-img project-img--placeholder" v-else>
                  <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="m9 9 6 6M15 9l-6 6"/></svg>
                </div>
                <div class="project-body">
                  <h3>{{ project.title }}</h3>
                  <p>{{ project.description?.length > 180 ? project.description.slice(0, 180) + '…' : project.description }}</p>
                  <div class="project-tags">
                    <span class="badge" v-for="tech in project.technologies" :key="tech">{{ tech }}</span>
                  </div>
                </div>
              </router-link>
            </div>
            <p v-else class="empty-msg page-anim page-stagger-3">No hay proyectos todavía.</p>
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
@keyframes spin { to { transform: rotate(360deg); } }

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.5rem;
}

.project-card {
  display: flex;
  flex-direction: column;
  color: inherit;
}

.project-img {
  aspect-ratio: 16 / 10;
  overflow: hidden;
  background: var(--c-gray-100);
}
.project-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s;
}
.project-card:hover .project-img img {
  transform: scale(1.04);
}

.project-img--placeholder {
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--c-gray-400);
}

.project-body {
  padding: 1rem 1.25rem;
  flex: 1;
  display: flex;
  flex-direction: column;
}
.project-body h3 {
  font-size: 1.05rem;
  margin-bottom: 0.35rem;
}
.project-body p {
  color: var(--color-text-muted);
  font-size: 0.9rem;
  line-height: 1.6;
  margin-bottom: 0.75rem;
  flex: 1;
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}

.empty-msg {
  text-align: center;
  color: var(--color-text-muted);
  padding: 3rem 0;
}

@media (max-width: 480px) {
  .projects-grid {
    grid-template-columns: 1fr;
  }
}
</style>
