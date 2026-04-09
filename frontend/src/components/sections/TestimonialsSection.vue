<script setup>
defineProps({
  testimonials: { type: Array, default: () => [] },
})
</script>

<template>
  <section id="testimonials" class="section section--slide" v-if="testimonials.length">
    <div class="container">
      <h2 class="section-title">Testimonios</h2>

      <div class="testimonials-grid">
        <div class="card testimonial-card" v-for="t in testimonials" :key="t.id">
          <div class="quote-mark">"</div>
          <p class="testimonial-text">{{ t.content }}</p>
          <div class="testimonial-footer">
            <img v-if="t.avatar" :src="t.avatar" :alt="t.name" class="testimonial-avatar" loading="lazy" />
            <div class="testimonial-avatar testimonial-avatar--placeholder" v-else>
              {{ t.name.charAt(0) }}
            </div>
            <div>
              <strong>{{ t.name }}</strong>
              <span v-if="t.position || t.company">{{ t.position }}<template v-if="t.company">, {{ t.company }}</template></span>
            </div>
          </div>
          <div class="testimonial-stars" v-if="t.rating">
            <span v-for="i in 5" :key="i" :class="{ filled: i <= t.rating }">★</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.section--slide {
  padding-top: 1.5rem;
  padding-bottom: 1rem;
}

.section--slide .section-title {
  margin-bottom: 0.5rem;
}

.section--slide .section-subtitle {
  margin-bottom: 1.5rem;
}

.testimonials-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1rem;
}

.testimonial-card {
  padding: 1.25rem;
  position: relative;
}

.quote-mark {
  position: absolute;
  top: 0.75rem;
  left: 1.25rem;
  font-size: 3.5rem;
  font-family: Georgia, serif;
  color: var(--c-accent-bg);
  line-height: 1;
  pointer-events: none;
  color: var(--color-accent);
  opacity: 0.15;
}

.testimonial-text {
  font-size: 0.88rem;
  line-height: 1.6;
  color: var(--color-text);
  margin-bottom: 1rem;
  font-style: italic;
}

.testimonial-footer {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 0.5rem;
}
.testimonial-footer strong {
  display: block;
  font-size: 0.9rem;
}
.testimonial-footer span {
  font-size: 0.8rem;
  color: var(--color-text-muted);
}

.testimonial-avatar {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  object-fit: cover;
  flex-shrink: 0;
}
.testimonial-avatar--placeholder {
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--c-accent-bg);
  color: var(--color-accent);
  font-weight: 700;
  font-size: 1.1rem;
}

.testimonial-stars {
  display: flex;
  gap: 2px;
  font-size: 0.9rem;
  color: var(--c-gray-300);
}
.testimonial-stars .filled {
  color: #f59e0b;
}
</style>
