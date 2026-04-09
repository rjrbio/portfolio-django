<script setup>
import { ref, onMounted, onUnmounted, watch, nextTick } from 'vue'
import { api } from '@/api/index.js'

import HeroSection from '@/components/sections/HeroSection.vue'
import ProjectsSection from '@/components/sections/ProjectsSection.vue'
import ServicesSection from '@/components/sections/ServicesSection.vue'
import TechSection from '@/components/sections/TechSection.vue'
import TestimonialsSection from '@/components/sections/TestimonialsSection.vue'
import ContactSection from '@/components/sections/ContactSection.vue'
import AppFooter from '@/components/AppFooter.vue'

const about = ref(null)
const projects = ref([])
const services = ref([])
const testimonials = ref([])
const technologies = ref([])
const loading = ref(true)
const error = ref(null)

/* ── Data fetching ─────────────────────────── */
onMounted(async () => {
  try {
    const [homeData, aboutData] = await Promise.all([
      api.home(),
      api.about(),
    ])

    projects.value = homeData.featured_projects || []
    services.value = homeData.services || []
    testimonials.value = homeData.testimonials || []

    about.value = aboutData.about || null
    technologies.value = aboutData.technologies || []
  } catch (e) {
    error.value = e
  } finally {
    loading.value = false
  }
})

/* ── Slideshow state ───────────────────────── */
const SLIDE_IDS = ['hero', 'projects', 'tech', 'contact']
const currentSlide = ref(0)
const leavingSlide = ref(-1)
const transitioning = ref(false)
const heroAnimated = ref(false)

const TRANSITION_MS = 900
const WHEEL_COOLDOWN = 1200
let lastWheelTime = 0

function goToSlide(index) {
  if (index === currentSlide.value || index < 0 || index >= SLIDE_IDS.length) return
  if (transitioning.value) return

  transitioning.value = true
  leavingSlide.value = currentSlide.value
  currentSlide.value = index

  // Broadcast active section to navbar
  window.dispatchEvent(new CustomEvent('slide-change', { detail: SLIDE_IDS[index] }))

  setTimeout(() => {
    leavingSlide.value = -1
    transitioning.value = false
  }, TRANSITION_MS)
}

function next() { goToSlide(currentSlide.value + 1) }
function prev() { goToSlide(currentSlide.value - 1) }

/* ── Wheel handler ─────────────────────────── */
function onWheel(e) {
  // If the active slide has scrollable content, check if we're at the edge
  const activeEl = document.querySelector('.slide.active')
  if (activeEl && activeEl.scrollHeight > activeEl.clientHeight) {
    const atTop = activeEl.scrollTop <= 0
    const atBottom = activeEl.scrollTop + activeEl.clientHeight >= activeEl.scrollHeight - 2
    if (e.deltaY < 0 && !atTop) return
    if (e.deltaY > 0 && !atBottom) return
  }

  e.preventDefault()
  const now = Date.now()
  if (now - lastWheelTime < WHEEL_COOLDOWN) return
  lastWheelTime = now

  if (e.deltaY > 0) next()
  else if (e.deltaY < 0) prev()
}

/* ── Touch handler ─────────────────────────── */
let touchStartY = 0
function onTouchStart(e) { touchStartY = e.touches[0].clientY }
function onTouchEnd(e) {
  const delta = touchStartY - e.changedTouches[0].clientY
  if (Math.abs(delta) < 50) return
  const now = Date.now()
  if (now - lastWheelTime < WHEEL_COOLDOWN) return
  lastWheelTime = now
  if (delta > 0) next()
  else prev()
}

/* ── Keyboard handler ──────────────────────── */
function onKeydown(e) {
  if (e.key === 'ArrowDown' || e.key === 'PageDown') { e.preventDefault(); next() }
  if (e.key === 'ArrowUp' || e.key === 'PageUp') { e.preventDefault(); prev() }
  if (e.key === 'Home') { e.preventDefault(); goToSlide(0) }
  if (e.key === 'End') { e.preventDefault(); goToSlide(SLIDE_IDS.length - 1) }
}

/* ── Mount / unmount ───────────────────────── */
const slideshowRef = ref(null)

onMounted(() => {
  window.addEventListener('keydown', onKeydown)
})
onUnmounted(() => {
  window.removeEventListener('keydown', onKeydown)
  if (slideshowRef.value) {
    slideshowRef.value.removeEventListener('wheel', onWheel)
    slideshowRef.value.removeEventListener('touchstart', onTouchStart)
    slideshowRef.value.removeEventListener('touchend', onTouchEnd)
  }
})

/* Attach wheel with { passive: false } after render */
watch(loading, async (isLoading) => {
  if (!isLoading && !error.value) {
    await nextTick()
    if (slideshowRef.value) {
      slideshowRef.value.addEventListener('wheel', onWheel, { passive: false })
      slideshowRef.value.addEventListener('touchstart', onTouchStart, { passive: true })
      slideshowRef.value.addEventListener('touchend', onTouchEnd, { passive: true })
    }
    // Small delay for DOM to paint, then animate Hero
    setTimeout(() => {
      heroAnimated.value = true
      window.dispatchEvent(new CustomEvent('slide-change', { detail: 'hero' }))
    }, 100)
  }
})

/* ── Navigate to slide by section id (for navbar) ───── */
function goToSection(sectionId) {
  const idx = SLIDE_IDS.indexOf(sectionId)
  if (idx !== -1) goToSlide(idx)
}

// Expose for navbar
onMounted(() => {
  window.__goToSection = goToSection
})
onUnmounted(() => {
  delete window.__goToSection
})
</script>

<template>
  <!-- Loading / Error (not in slideshow) -->
  <div v-if="loading" class="loading-screen" style="margin-top: var(--nav-height)">
    <div class="spinner"></div>
    <p>Cargando portafolio…</p>
  </div>

  <div v-else-if="error" class="loading-screen" style="margin-top: var(--nav-height)">
    <p style="color: #b91c1c">Error al cargar los datos. Refresca la página.</p>
  </div>

  <!-- Slideshow -->
  <div
    v-else
    ref="slideshowRef"
    class="slideshow"
  >
    <!-- Slide 0: Hero -->
    <div
      class="slide"
      :class="{ active: currentSlide === 0, leaving: leavingSlide === 0 }"
    >
      <HeroSection :about="about" :animate="heroAnimated" />
    </div>

    <!-- Slide 1: Projects + Services (horizontal) -->
    <div
      class="slide"
      :class="{ active: currentSlide === 1, leaving: leavingSlide === 1 }"
    >
      <div class="slide-horizontal">
        <div class="slide-content slide-stagger-1 slide-col">
          <ProjectsSection :projects="projects" />
        </div>
        <div class="slide-content slide-stagger-2 slide-col">
          <ServicesSection :services="services" />
        </div>
      </div>
    </div>

    <!-- Slide 2: Tech -->
    <div
      class="slide"
      :class="{ active: currentSlide === 2, leaving: leavingSlide === 2 }"
    >
      <TechSection :technologies="technologies" :activate="currentSlide === 2" />
    </div>

    <!-- Slide 3: Testimonials + Contact + Footer -->
    <div
      class="slide"
      :class="{ active: currentSlide === 3, leaving: leavingSlide === 3 }"
    >
      <div class="slide-inner">
        <div class="slide-content slide-stagger-1">
          <TestimonialsSection :testimonials="testimonials" />
        </div>
        <div class="slide-content slide-stagger-2">
          <ContactSection />
        </div>
        <div class="slide-content slide-stagger-3">
          <AppFooter :about="about" />
        </div>
      </div>
    </div>

    <!-- Navigation dots -->
    <div class="slide-dots">
      <button
        v-for="(id, i) in SLIDE_IDS"
        :key="id"
        class="slide-dot"
        :class="{ active: currentSlide === i }"
        :aria-label="'Ir a sección ' + id"
        @click="goToSlide(i)"
      ></button>
    </div>
  </div>
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

.slide-inner {
  height: 100%;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 1rem 0;
}

.slide-horizontal {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem 1.5rem;
  gap: 2rem;
  max-width: var(--container-max);
  margin: 0 auto;
}

.slide-col {
  flex: 1;
  min-width: 0;
  overflow-y: auto;
}
</style>
