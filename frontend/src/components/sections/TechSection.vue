<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  technologies: { type: Array, default: () => [] },
  activate: { type: Boolean, default: false },
})

const iconsVisible = ref(false)

// Trigger icon animation when the slide becomes active
watch(() => props.activate, (active) => {
  if (active && !iconsVisible.value) {
    iconsVisible.value = true
  }
})

function iconDelay(index) {
  return { transitionDelay: `${index * 60}ms` }
}
</script>

<template>
  <section id="tech" class="tech-panel">
    <div class="container">
      <h2 class="section-title tech-title">Tecnologías</h2>
      <div class="tech-cloud">
        <div
          v-for="(tech, i) in technologies"
          :key="tech.id"
          class="tech-icon-item"
          :class="{ visible: iconsVisible }"
          :style="iconDelay(i)"
        >
          <i v-if="tech.icon_class" :class="tech.icon_class" class="tech-icon"></i>
          <span class="tech-label">{{ tech.name }}</span>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.tech-panel {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--color-bg);
}

.tech-title {
  text-align: center;
  margin-bottom: 3rem;
}

.tech-cloud {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 2rem;
  max-width: 900px;
  margin: 0 auto;
}

.tech-icon-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.4rem;
  width: 72px;
  /* animation handled by global CSS class */
}

.tech-icon {
  font-size: 2.5rem;
  color: var(--color-heading);
  transition: color 0.2s, transform 0.2s;
}

.tech-icon-item:hover .tech-icon {
  color: var(--color-accent);
  transform: scale(1.15);
}

.tech-label {
  font-size: 0.7rem;
  font-weight: 600;
  color: var(--color-text-muted);
  text-align: center;
  line-height: 1.2;
}

@media (max-width: 768px) {
  .tech-cloud {
    gap: 1.25rem;
  }
  .tech-icon-item {
    width: 60px;
  }
  .tech-icon {
    font-size: 2rem;
  }
}
</style>
