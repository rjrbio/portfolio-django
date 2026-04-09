<script setup>
import { ref, onMounted, nextTick } from 'vue'
import { api } from '@/api/index.js'
import AppFooter from '@/components/AppFooter.vue'

const experience = ref([])
const education = ref([])
const cvFile = ref(null)
const about = ref(null)
const loading = ref(true)
const error = ref(null)
const ready = ref(false)

onMounted(async () => {
  try {
    const [resumeData, aboutData] = await Promise.all([
      api.resume(),
      api.about(),
    ])
    experience.value = resumeData.experience || []
    education.value = resumeData.education || []
    cvFile.value = resumeData.about?.cv_file || null
    about.value = aboutData.about || null
  } catch (e) {
    error.value = e
  } finally {
    loading.value = false
    await nextTick()
    requestAnimationFrame(() => { ready.value = true })
  }
})

function formatDate(d) {
  if (!d) return ''
  const date = new Date(d)
  return date.toLocaleDateString('es-ES', { month: 'short', year: 'numeric' })
}
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
            <h1 class="section-title page-anim page-stagger-1">Currículum</h1>
            <p class="section-subtitle page-anim page-stagger-2">Mi trayectoria profesional y formación</p>

            <div class="resume-columns page-anim page-stagger-3">
            <div class="resume-col" v-if="experience.length">
              <h3 class="resume-col-title">Experiencia</h3>
              <div class="timeline">
                <div class="timeline-item" v-for="exp in experience" :key="exp.id">
                  <div class="timeline-dot"></div>
                  <div class="timeline-content">
                    <h4>{{ exp.position }}</h4>
                    <span class="timeline-company">{{ exp.company }}</span>
                    <span class="timeline-date">
                      {{ formatDate(exp.start_date) }} – {{ exp.current ? 'Actualidad' : formatDate(exp.end_date) }}
                    </span>
                    <p v-if="exp.description">{{ exp.description }}</p>
                  </div>
                </div>
              </div>
            </div>

            <div class="resume-col" v-if="education.length">
              <h3 class="resume-col-title">Educación</h3>
              <div class="timeline">
                <div class="timeline-item" v-for="edu in education" :key="edu.id">
                  <div class="timeline-dot"></div>
                  <div class="timeline-content">
                    <h4>{{ edu.degree }}</h4>
                    <span class="timeline-company">{{ edu.institution }}</span>
                    <span class="timeline-date">
                      {{ formatDate(edu.start_date) }} – {{ edu.current ? 'Actualidad' : formatDate(edu.end_date) }}
                    </span>
                    <p v-if="edu.description">{{ edu.description }}</p>
                  </div>
                </div>
              </div>
            </div>
            </div>

            <div class="resume-download page-anim page-stagger-4" v-if="cvFile">
              <a :href="cvFile" target="_blank" rel="noopener" class="btn btn-primary">
                Descargar CV completo
              </a>
            </div>
          </div>
        </section>
        <div class="page-anim page-stagger-5">
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

.resume-columns {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
}

.resume-col-title {
  font-size: 1.1rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--color-accent);
  margin-bottom: 1.5rem;
}

.timeline {
  position: relative;
  padding-left: 1.5rem;
  border-left: 2px solid var(--c-gray-200);
}

.timeline-item {
  position: relative;
  padding-bottom: 2rem;
}
.timeline-item:last-child {
  padding-bottom: 0;
}

.timeline-dot {
  position: absolute;
  left: -1.625rem;
  top: 0.35rem;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--color-accent);
  border: 2px solid var(--color-bg);
  box-shadow: 0 0 0 2px var(--color-accent);
}

.timeline-content h4 {
  font-size: 1rem;
  margin-bottom: 0.15rem;
}

.timeline-company {
  display: block;
  font-weight: 600;
  font-size: 0.9rem;
  color: var(--color-text-muted);
}

.timeline-date {
  display: inline-block;
  font-size: 0.8rem;
  color: var(--color-text-muted);
  margin: 0.25rem 0 0.5rem;
  background: var(--c-gray-100);
  padding: 0.15rem 0.5rem;
  border-radius: var(--radius-sm);
}

.timeline-content p {
  font-size: 0.9rem;
  line-height: 1.6;
  color: var(--color-text-muted);
}

.resume-download {
  text-align: center;
  margin-top: 3rem;
}

@media (max-width: 768px) {
  .resume-columns {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
}
</style>
