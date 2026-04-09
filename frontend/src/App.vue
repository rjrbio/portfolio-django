<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import ChatBot from '@/components/ChatBot.vue'

const route = useRoute()
const router = useRouter()
const isLanding = computed(() => route.path === '/')

/* ── Navbar ─────────────────────────────────────── */
const sectionLinks = [
  { label: 'Inicio', hash: '#hero', section: 'hero' },
  { label: 'Servicios', hash: '#services', section: 'projects' },
  { label: 'Tech', hash: '#tech', section: 'tech' },
  { label: 'Contacto', hash: '#contact', section: 'contact' },
]

const routeLinks = [
  { label: 'Proyectos', to: '/projects' },
  { label: 'Sobre mí', to: '/about' },
  { label: 'Blog', to: '/blog' },
  { label: 'Currículum', to: '/resume' },
]

const mobileOpen = ref(false)
const activeSection = ref('hero')
const scrolled = ref(false)

/* Listen to slide-change events from the slideshow */
function onSlideChange(e) {
  activeSection.value = e.detail
  scrolled.value = activeSection.value !== 'hero'
}

function onScroll() {
  if (!isLanding.value) {
    scrolled.value = window.scrollY > 20
  }
}

onMounted(() => {
  window.addEventListener('slide-change', onSlideChange)
  window.addEventListener('scroll', onScroll, { passive: true })
})
onUnmounted(() => {
  window.removeEventListener('slide-change', onSlideChange)
  window.removeEventListener('scroll', onScroll)
})

function sectionClick(section) {
  mobileOpen.value = false
  if (!isLanding.value) {
    window.location.href = '/'
    return
  }
  // Use the slideshow navigation
  if (window.__goToSection) {
    window.__goToSection(section)
  }
}

function routeClick(to) {
  mobileOpen.value = false
  router.push(to)
}
</script>

<template>
  <header class="navbar" :class="{ scrolled }">
    <div class="container nav-inner">
      <a href="/#hero" class="nav-logo" @click="mobileOpen = false">Portfolio</a>

      <button class="nav-toggle" @click="mobileOpen = !mobileOpen" :aria-label="mobileOpen ? 'Cerrar menú' : 'Abrir menú'">
        <span :class="{ open: mobileOpen }"></span>
      </button>

      <nav :class="{ open: mobileOpen }">
        <a
          v-for="link in sectionLinks"
          :key="link.hash"
          :href="link.hash"
          :class="{ active: isLanding && activeSection === link.section }"
          @click.prevent="sectionClick(link.section)"
        >
          {{ link.label }}
        </a>
        <a
          v-for="link in routeLinks"
          :key="link.to"
          href="#"
          :class="{ active: route.path === link.to }"
          @click.prevent="routeClick(link.to)"
        >
          {{ link.label }}
        </a>
      </nav>
    </div>
  </header>

  <RouterView />

  <ChatBot />
</template>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  height: var(--nav-height);
  display: flex;
  align-items: center;
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  transition: box-shadow 0.3s, background 0.3s;
}
.navbar.scrolled {
  box-shadow: 0 1px 8px rgba(0, 0, 0, 0.06);
  background: rgba(255, 255, 255, 0.95);
}

.nav-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav-logo {
  font-weight: 800;
  font-size: 1.2rem;
  color: var(--color-heading);
  letter-spacing: -0.02em;
}
.nav-logo:hover { color: var(--color-accent); }

nav {
  display: flex;
  gap: 0.25rem;
}
nav a {
  padding: 0.4rem 0.75rem;
  border-radius: var(--radius-sm);
  font-size: 0.88rem;
  font-weight: 500;
  color: var(--color-text-muted);
  transition: color 0.2s, background 0.2s;
}
nav a:hover {
  color: var(--color-heading);
  background: var(--c-gray-100);
}
nav a.active {
  color: var(--color-accent);
  background: var(--c-accent-bg);
}

/* Toggle */
.nav-toggle {
  display: none;
  background: none;
  border: none;
  padding: 0.5rem;
}
.nav-toggle span,
.nav-toggle span::before,
.nav-toggle span::after {
  display: block;
  width: 22px;
  height: 2px;
  background: var(--color-heading);
  border-radius: 2px;
  transition: 0.3s;
  position: relative;
}
.nav-toggle span::before,
.nav-toggle span::after {
  content: '';
  position: absolute;
  left: 0;
  width: 100%;
}
.nav-toggle span::before { top: -7px; }
.nav-toggle span::after { top: 7px; }
.nav-toggle span.open { background: transparent; }
.nav-toggle span.open::before { top: 0; transform: rotate(45deg); }
.nav-toggle span.open::after { top: 0; transform: rotate(-45deg); }

@media (max-width: 768px) {
  .nav-toggle { display: block; }
  nav {
    position: fixed;
    top: var(--nav-height);
    left: 0;
    right: 0;
    background: var(--color-bg);
    flex-direction: column;
    padding: 1rem;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    transform: translateY(-120%);
    opacity: 0;
    transition: transform 0.3s, opacity 0.3s;
    pointer-events: none;
  }
  nav.open {
    transform: translateY(0);
    opacity: 1;
    pointer-events: auto;
  }
  nav a {
    padding: 0.65rem 1rem;
    font-size: 1rem;
  }
}
</style>

