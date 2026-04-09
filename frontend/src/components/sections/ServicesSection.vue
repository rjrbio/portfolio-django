<script setup>
defineProps({
  services: { type: Array, default: () => [] },
})
</script>

<template>
  <section id="services" class="section section--slide">
    <div class="container">
      <h2 class="section-title">Servicios</h2>

      <div class="services-grid">
        <div class="card service-card" v-for="service in services" :key="service.id">
          <div class="service-icon" v-if="service.icon">
            <i :class="service.icon"></i>
          </div>
          <h3>{{ service.title }}</h3>
          <p>{{ service.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.services-grid {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.section--slide {
  padding-top: 1rem;
  padding-bottom: 1rem;
}

.service-card {
  padding: 1.25rem 1rem;
  text-align: center;
}

.service-icon {
  font-size: 1.5rem;
  color: var(--color-accent);
  margin-bottom: 0.5rem;
}

.service-card h3 {
  font-size: 1rem;
  margin-bottom: 0.5rem;
}

.service-card p {
  color: var(--color-text-muted);
  font-size: 0.85rem;
  line-height: 1.6;
}
</style>
