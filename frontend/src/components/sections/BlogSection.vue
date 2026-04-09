<script setup>
defineProps({
  posts: { type: Array, default: () => [] },
})
</script>

<template>
  <section id="blog" class="section section-alt fade-section" v-if="posts.length">
    <div class="container">
      <h2 class="section-title">Blog</h2>
      <p class="section-subtitle">Artículos y reflexiones</p>

      <div class="blog-grid">
        <router-link
          v-for="post in posts"
          :key="post.id"
          :to="`/blog/${post.slug}`"
          class="card blog-card"
        >
          <div class="blog-img" v-if="post.image">
            <img :src="post.image" :alt="post.title" />
          </div>
          <div class="blog-body">
            <time v-if="post.created_at">{{ new Date(post.created_at).toLocaleDateString('es-ES', { day: 'numeric', month: 'long', year: 'numeric' }) }}</time>
            <h3>{{ post.title }}</h3>
            <p>{{ post.excerpt }}</p>
          </div>
        </router-link>
      </div>
    </div>
  </section>
</template>

<style scoped>
.blog-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.5rem;
}

.blog-card {
  display: flex;
  flex-direction: column;
  color: inherit;
}

.blog-img {
  aspect-ratio: 16 / 9;
  overflow: hidden;
  background: var(--c-gray-100);
}
.blog-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s;
}
.blog-card:hover .blog-img img {
  transform: scale(1.04);
}

.blog-body {
  padding: 1.25rem;
  flex: 1;
}

.blog-body time {
  font-size: 0.8rem;
  color: var(--color-text-muted);
  text-transform: uppercase;
  letter-spacing: 0.03em;
}

.blog-body h3 {
  font-size: 1.1rem;
  margin: 0.4rem 0 0.5rem;
}

.blog-body p {
  color: var(--color-text-muted);
  font-size: 0.9rem;
  line-height: 1.6;
}

@media (max-width: 480px) {
  .blog-grid {
    grid-template-columns: 1fr;
  }
}
</style>
