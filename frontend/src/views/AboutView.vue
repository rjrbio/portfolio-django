<script setup>
import { ref, onMounted, nextTick } from 'vue'
import { api } from '@/api/index.js'
import AppFooter from '@/components/AppFooter.vue'

const about = ref(null)
const technologies = ref([])
const loading = ref(true)
const error = ref(null)
const ready = ref(false)

onMounted(async () => {
    try {
        const aboutData = await api.about()
        about.value = aboutData.about || null
        technologies.value = aboutData.technologies || []
    } catch (e) {
        error.value = e
    } finally {
        loading.value = false
        await nextTick()
        requestAnimationFrame(() => { ready.value = true })
    }
})
</script>

<template>
    <main style="padding-top: var(--nav-height)">
        <div v-if="loading" class="loading-screen">
            <div class="spinner"></div>
            <p>Cargando…</p>
        </div>

        <div v-else-if="error" class="loading-screen">
            <p style="color: #b91c1c">Error al cargar los datos.</p>
        </div>

        <template v-else>
            <div class="page-enter" :class="{ ready }">
                <section class="section" v-if="about">
                    <div class="container">
                        <h1 class="section-title page-anim page-stagger-1">Sobre mí</h1>

                        <div class="about-layout">
                            <div class="about-photo page-anim page-stagger-2" v-if="about.profile_image">
                                <img :src="about.profile_image" :alt="about.name" />
                            </div>
                            <div class="about-content page-anim page-stagger-3">
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
                                <a v-if="about.cv_file" :href="about.cv_file" target="_blank" rel="noopener"
                                    class="btn btn-outline" style="margin-top:1.5rem">
                                    Descargar CV
                                </a>
                            </div>
                        </div>
                    </div>
                </section>
                <div class="page-anim page-stagger-4">
                    <AppFooter :about="about" />
                </div>
            </div>
        </template>
    </main>
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
    to {
        transform: rotate(360deg);
    }
}

.about-layout {
    max-width: 800px;
    margin: 0 auto;
    display: flex;
    gap: 3rem;
    align-items: flex-start;
}

.about-photo {
    flex-shrink: 0;
    width: 240px;
}

.about-photo img {
    width: 100%;
    height: auto;
    border-radius: 50%;
}

.about-content {
    flex: 1;
}

.about-bio {
    font-size: 1.05rem;
    line-height: 1.8;
    color: var(--color-text);
    margin-bottom: 1.5rem;
    text-align: justify;
}

.about-details {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
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
    .about-layout {
        flex-direction: column;
        align-items: center;
        text-align: center;
    }

    .about-photo {
        width: 180px;
    }

    .about-details {
        align-items: center;
    }

    .about-details li {
        flex-direction: column;
        gap: 0.25rem;
    }
}
</style>
