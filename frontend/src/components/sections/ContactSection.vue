<script setup>
import { ref } from 'vue'
import { api } from '@/api/index.js'

const form = ref({ name: '', email: '', subject: '', message: '' })
const success = ref(false)
const errors = ref(null)
const submitting = ref(false)

async function submit() {
  submitting.value = true
  errors.value = null
  try {
    await api.contact(form.value)
    success.value = true
    form.value = { name: '', email: '', subject: '', message: '' }
  } catch (e) {
    errors.value = e.data
  } finally {
    submitting.value = false
  }
}
</script>

<template>
  <section id="contact" class="section section--slide section-alt">
    <div class="container">
      <h2 class="section-title">Contacto</h2>

      <div class="contact-wrapper">
        <div v-if="success" class="contact-success">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--color-accent)" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
          <h3>¡Mensaje enviado!</h3>
          <p>Gracias por tu interés. Te responderé lo antes posible.</p>
          <button class="btn btn-outline" @click="success = false">Enviar otro mensaje</button>
        </div>

        <form v-else @submit.prevent="submit" class="contact-form">
          <div v-if="errors" class="form-errors">
            <p v-for="(msgs, field) in errors" :key="field">
              <strong>{{ field }}:</strong> {{ Array.isArray(msgs) ? msgs.join(', ') : msgs }}
            </p>
          </div>

          <div class="form-row">
            <div class="form-group">
              <label for="c-name">Nombre</label>
              <input id="c-name" v-model="form.name" required placeholder="Tu nombre" />
            </div>
            <div class="form-group">
              <label for="c-email">Email</label>
              <input id="c-email" v-model="form.email" type="email" required placeholder="tu@email.com" />
            </div>
          </div>

          <div class="form-group">
            <label for="c-subject">Asunto</label>
            <input id="c-subject" v-model="form.subject" required placeholder="¿De qué quieres hablar?" />
          </div>

          <div class="form-group">
            <label for="c-message">Mensaje</label>
            <textarea id="c-message" v-model="form.message" required rows="5" placeholder="Cuéntame los detalles de tu proyecto…"></textarea>
          </div>

          <button type="submit" class="btn btn-primary" :disabled="submitting">
            {{ submitting ? 'Enviando…' : 'Enviar mensaje' }}
          </button>
        </form>
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
  margin-bottom: 0.75rem;
}

.contact-wrapper {
  max-width: 640px;
  margin: 0 auto;
}

.contact-success {
  text-align: center;
  padding: 3rem 0;
}
.contact-success h3 {
  margin: 1rem 0 0.5rem;
}
.contact-success p {
  color: var(--color-text-muted);
  margin-bottom: 1.5rem;
}

.contact-form {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.form-errors {
  background: #fef2f2;
  border: 1px solid #fca5a5;
  border-radius: var(--radius-md);
  padding: 0.75rem 1rem;
  color: #b91c1c;
  font-size: 0.9rem;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
}

.form-group label {
  font-weight: 600;
  font-size: 0.9rem;
  color: var(--color-heading);
}

.form-group input,
.form-group textarea {
  border: 1.5px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: 0.65rem 0.85rem;
  font: inherit;
  font-size: 0.95rem;
  color: var(--color-text);
  background: var(--color-bg);
  outline: none;
  transition: border-color 0.2s;
}
.form-group input:focus,
.form-group textarea:focus {
  border-color: var(--color-accent);
}
.form-group textarea {
  resize: vertical;
}

@media (max-width: 480px) {
  .form-row {
    grid-template-columns: 1fr;
  }
}
</style>
