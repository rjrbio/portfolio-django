<script setup>
defineProps({
  about: { type: Object, default: null },
  technologies: { type: Array, default: () => [] },
})
</script>

<template>
  <section id="about" class="section section--compact">
    <div class="container">
      <h2 class="section-title">Sobre mí</h2>

      <div class="about-grid" v-if="about">
        <div class="about-content">
          <p class="about-bio">{{ about.bio }}</p>
          <ul class="about-details">
            <li v-if="about.location">
              <span class="detail-label">Ubicación</span>
              <span>{{ about.location }}</span>
            </li>
            <li v-if="about.email">
              <span class="detail-label">Email</span>
              <a :href="`mailto:${about.email}`">{{ about.email }}</a>
            </li>
          </ul>
          <a v-if="about.cv_file" :href="about.cv_file" target="_blank" rel="noopener" class="btn btn-outline" style="margin-top:1rem">
            Descargar CV
          </a>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.section--compact {
  padding-top: 2rem;
  padding-bottom: 1.5rem;
}

.about-grid {
  max-width: 900px;
  margin: 0 auto;
}

.about-content {
  background: var(--color-bg);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-sm);
  padding: 1.25rem 1.5rem;
}

.about-bio {
  font-size: 0.95rem;
  line-height: 1.7;
  color: var(--color-text);
  margin-bottom: 1rem;
  text-align: justify;
}

.about-details {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}
.about-details li {
  display: flex;
  gap: 0.75rem;
}
.detail-label {
  font-weight: 600;
  min-width: 90px;
  color: var(--color-heading);
}

@media (max-width: 768px) {
  .about-content {
    padding: 1.25rem;
  }
}
</style>
