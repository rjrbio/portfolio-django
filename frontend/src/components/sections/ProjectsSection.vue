<script setup>
defineProps({
  projects: { type: Array, default: () => [] },
})
</script>

<template>
  <section id="projects" class="section section--slide">
    <div class="container">
      <h2 class="section-title">Proyecto destacado</h2>

      <div class="projects-grid">
        <router-link
          v-for="project in projects"
          :key="project.id"
          :to="`/projects/${project.slug}`"
          class="card project-card"
        >
          <div class="project-img" v-if="project.image">
            <img :src="project.image" :alt="project.title" />
          </div>
          <div class="project-img project-img--placeholder" v-else>
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="m9 9 6 6M15 9l-6 6"/></svg>
          </div>
          <div class="project-body">
            <h3>{{ project.title }}</h3>
            <p>{{ project.description?.length > 120 ? project.description.slice(0, 120) + '…' : project.description }}</p>
            <div class="project-tags">
              <span class="badge" v-for="tech in project.technologies" :key="tech">{{ tech }}</span>
            </div>
          </div>
        </router-link>
      </div>

      <div class="projects-more">
        <router-link to="/projects" class="btn btn-outline">Ver todos los proyectos</router-link>
      </div>
    </div>
  </section>
</template>

<style scoped>
.section--slide {
  padding-top: 1rem;
  padding-bottom: 1rem;
}

.projects-grid {
  display: flex;
  flex-direction: column;
  gap: 1rem;
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
  padding: 0.75rem 1rem;
  flex: 1;
  display: flex;
  flex-direction: column;
}
.project-body h3 {
  font-size: 1rem;
  margin-bottom: 0.25rem;
}
.project-body p {
  color: var(--color-text-muted);
  font-size: 0.85rem;
  line-height: 1.5;
  margin-bottom: 0.5rem;
  flex: 1;
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}

.projects-more {
  text-align: center;
  margin-top: 1rem;
}

@media (max-width: 480px) {
  .projects-grid {
    grid-template-columns: 1fr;
  }
}
</style>
