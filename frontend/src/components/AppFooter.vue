<script setup>
defineProps({
  about: { type: Object, default: null },
})
</script>

<template>
  <footer class="site-footer">
    <div class="container footer-inner">
      <div class="footer-left">
        <strong>{{ about?.name ?? 'Portfolio' }}</strong>
        <p>&copy; {{ new Date().getFullYear() }}. Todos los derechos reservados.</p>
      </div>
      <div class="footer-links" v-if="about">
        <a v-if="about.github" :href="about.github" target="_blank" rel="noopener">GitHub</a>
        <a v-if="about.linkedin" :href="about.linkedin" target="_blank" rel="noopener">LinkedIn</a>
        <a v-if="about.twitter" :href="about.twitter" target="_blank" rel="noopener">Twitter</a>
        <a v-if="about.email" :href="`mailto:${about.email}`">Email</a>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.site-footer {
  border-top: 1px solid var(--color-border);
  padding: 1.25rem 0;
  background: var(--c-gray-50);
}

.footer-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
}

.footer-left strong {
  display: block;
  font-size: 1rem;
  color: var(--color-heading);
  margin-bottom: 0.15rem;
}
.footer-left p {
  font-size: 0.85rem;
  color: var(--color-text-muted);
}

.footer-links {
  display: flex;
  gap: 1.25rem;
}
.footer-links a {
  font-size: 0.9rem;
  color: var(--color-text-muted);
  transition: color 0.2s;
}
.footer-links a:hover {
  color: var(--color-accent);
}

@media (max-width: 480px) {
  .footer-inner {
    flex-direction: column;
    text-align: center;
  }
}
</style>
