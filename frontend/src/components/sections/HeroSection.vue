<script setup>
defineProps({
  about: { type: Object, default: null },
  animate: { type: Boolean, default: false },
})

function goContact() {
  if (window.__goToSection) window.__goToSection('contact')
}
</script>

<template>
  <section id="hero" class="hero hero-anim" :class="{ animate }">
    <div class="container hero-inner">
      <div class="hero-text">
        <p class="hero-greeting">Hola, soy</p>
        <h1 class="hero-name">{{ about?.name ?? 'Desarrollador' }}</h1>
        <p class="hero-title">{{ about?.title ?? 'Full-Stack Developer' }}</p>
        <p class="hero-bio">{{ 'Aprendiendo hoy para construir el software de mañana' }}</p>
        <div class="hero-actions">
          <router-link to="/projects" class="btn btn-primary">Ver proyectos</router-link>
          <button class="btn btn-outline" @click="goContact">Contacto</button>
        </div>
        <div class="hero-socials" v-if="about">
          <a v-if="about.github" :href="about.github" target="_blank" rel="noopener" aria-label="GitHub">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .5C5.37.5 0 5.78 0 12.29c0 5.21 3.438 9.63 8.205 11.19.6.11.82-.26.82-.577v-2.17c-3.338.726-4.042-1.416-4.042-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.09-.745.083-.73.083-.73 1.205.085 1.84 1.237 1.84 1.237 1.07 1.835 2.807 1.305 3.492.997.108-.776.42-1.305.762-1.605-2.665-.302-5.466-1.332-5.466-5.93 0-1.31.468-2.382 1.236-3.222-.124-.303-.536-1.523.116-3.176 0 0 1.008-.322 3.3 1.23A11.5 11.5 0 0112 6.844c1.02.005 2.047.138 3.006.404 2.29-1.553 3.296-1.23 3.296-1.23.654 1.653.242 2.873.118 3.176.77.84 1.234 1.911 1.234 3.222 0 4.61-2.805 5.625-5.476 5.922.43.372.823 1.102.823 2.222v3.293c0 .32.218.694.825.576C20.565 21.917 24 17.506 24 12.29 24 5.78 18.627.5 12 .5z"/></svg>
          </a>
          <a v-if="about.linkedin" :href="about.linkedin" target="_blank" rel="noopener" aria-label="LinkedIn">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
          </a>
          <a v-if="about.twitter" :href="about.twitter" target="_blank" rel="noopener" aria-label="Twitter">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
          </a>
        </div>
      </div>
      <div class="hero-image" v-if="about?.profile_image">
        <img :src="about.profile_image" :alt="about.name" />
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero {
  min-height: calc(100vh - var(--nav-height));
  display: flex;
  align-items: center;
  background: linear-gradient(135deg, var(--c-gray-50) 0%, var(--c-white) 100%);
}

.hero-inner {
  display: flex;
  align-items: center;
  gap: 4rem;
  padding-top: 3rem;
  padding-bottom: 3rem;
}

.hero-text {
  flex: 1;
}

.hero-greeting {
  font-size: 1.1rem;
  color: var(--color-accent);
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.hero-name {
  font-size: clamp(2.5rem, 5vw, 3.5rem);
  margin-bottom: 0.5rem;
}

.hero-title {
  font-size: 1.25rem;
  color: var(--color-text-muted);
  margin-bottom: 1rem;
}

.hero-bio {
  color: var(--color-text-muted);
  max-width: 520px;
  margin-bottom: 1.5rem;
  line-height: 1.7;
}

.hero-actions {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
}

.hero-socials {
  display: flex;
  gap: 1rem;
}
.hero-socials a {
  color: var(--color-text-muted);
  transition: color 0.2s;
}
.hero-socials a:hover {
  color: var(--color-accent);
}

.hero-image {
  flex-shrink: 0;
  width: 300px;
  height: 300px;
  overflow: hidden;
  border-radius: 50%;
}
.hero-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

@media (max-width: 768px) {
  .hero-inner {
    flex-direction: column-reverse;
    text-align: center;
    gap: 2rem;
  }
  .hero-actions,
  .hero-socials {
    justify-content: center;
  }
  .hero-bio {
    margin-left: auto;
    margin-right: auto;
  }
  .hero-image {
    width: 200px;
    height: 200px;
  }
}
</style>
