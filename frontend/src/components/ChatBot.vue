<script setup>
import { ref, nextTick } from 'vue'
import { api } from '@/api/index.js'

const open = ref(false)
const messages = ref([
  {
    role: 'assistant',
    text: '¡Hola! Soy el asistente de IA de este portafolio. Puedo responder preguntas sobre proyectos, habilidades técnicas, experiencia y servicios. ¿En qué puedo ayudarte?',
  },
])
const input = ref('')
const loading = ref(false)
const chatEl = ref(null)

async function scrollToBottom() {
  await nextTick()
  if (chatEl.value) {
    chatEl.value.scrollTop = chatEl.value.scrollHeight
  }
}

async function send() {
  const question = input.value.trim()
  if (!question || loading.value) return

  messages.value.push({ role: 'user', text: question })
  input.value = ''
  loading.value = true
  await scrollToBottom()

  try {
    const data = await api.agent(question)
    messages.value.push({ role: 'assistant', text: data.answer })
  } catch (e) {
    const msg = e?.data?.error || 'Ocurrió un error. Inténtalo de nuevo.'
    messages.value.push({ role: 'assistant', text: msg, isError: true })
  } finally {
    loading.value = false
    await scrollToBottom()
  }
}

function handleKeydown(e) {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault()
    send()
  }
}
</script>

<template>
  <!-- Floating button -->
  <button class="chat-fab" @click="open = !open" :aria-label="open ? 'Cerrar chat' : 'Abrir asistente IA'">
    <svg v-if="!open" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 21 1.9-5.7a8.5 8.5 0 1 1 3.8 3.8z"/></svg>
    <svg v-else width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
  </button>

  <!-- Chat panel -->
  <Transition name="chat-slide">
    <div v-if="open" class="chat-panel">
      <div class="chat-header">
        <strong>Asistente IA</strong>
        <span>Pregúntame sobre el portafolio</span>
      </div>

      <div ref="chatEl" class="chat-messages">
        <div
          v-for="(msg, i) in messages"
          :key="i"
          class="msg"
          :class="[msg.role, { error: msg.isError }]"
        >
          <div class="msg-bubble">
            <p>{{ msg.text }}</p>
          </div>
        </div>
        <div v-if="loading" class="msg assistant">
          <div class="msg-bubble">
            <span class="typing"><span></span><span></span><span></span></span>
          </div>
        </div>
      </div>

      <div class="chat-input">
        <textarea
          v-model="input"
          placeholder="Escribe tu pregunta…"
          :disabled="loading"
          rows="1"
          @keydown="handleKeydown"
        />
        <button :disabled="loading || !input.trim()" @click="send" aria-label="Enviar">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M2.01 21 23 12 2.01 3 2 10l15 2-15 2z"/></svg>
        </button>
      </div>
    </div>
  </Transition>
</template>

<style scoped>
.chat-fab {
  position: fixed;
  bottom: 1.5rem;
  right: 1.5rem;
  z-index: 1000;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  border: none;
  background: var(--color-accent);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.35);
  transition: transform 0.2s, box-shadow 0.2s;
}
.chat-fab:hover {
  transform: scale(1.06);
  box-shadow: 0 6px 20px rgba(37, 99, 235, 0.4);
}

/* Panel */
.chat-panel {
  position: fixed;
  bottom: 5.5rem;
  right: 1.5rem;
  z-index: 999;
  width: 380px;
  max-height: 520px;
  display: flex;
  flex-direction: column;
  background: var(--color-bg);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.12);
  overflow: hidden;
}

.chat-header {
  padding: 0.85rem 1rem;
  border-bottom: 1px solid var(--color-border);
  background: var(--c-gray-50);
}
.chat-header strong {
  display: block;
  font-size: 0.95rem;
}
.chat-header span {
  font-size: 0.75rem;
  color: var(--color-text-muted);
}

.chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  min-height: 260px;
}

.msg { display: flex; }
.msg.user { justify-content: flex-end; }
.msg.assistant { justify-content: flex-start; }

.msg-bubble {
  max-width: 80%;
  padding: 0.6rem 0.85rem;
  border-radius: var(--radius-md);
  font-size: 0.88rem;
  line-height: 1.5;
  background: var(--c-gray-100);
}
.msg.user .msg-bubble {
  background: var(--color-accent);
  color: #fff;
}
.msg.error .msg-bubble {
  background: #fef2f2;
  color: #b91c1c;
  border: 1px solid #fca5a5;
}
.msg-bubble p { margin: 0; white-space: pre-wrap; }

/* Typing */
.typing { display: flex; gap: 4px; align-items: center; height: 18px; }
.typing span {
  width: 6px; height: 6px; border-radius: 50%;
  background: currentColor; opacity: 0.3;
  animation: tb 1.2s infinite;
}
.typing span:nth-child(2) { animation-delay: 0.2s; }
.typing span:nth-child(3) { animation-delay: 0.4s; }
@keyframes tb {
  0%, 80%, 100% { transform: translateY(0); opacity: 0.3; }
  40% { transform: translateY(-5px); opacity: 1; }
}

/* Input */
.chat-input {
  display: flex;
  gap: 0.5rem;
  padding: 0.75rem;
  border-top: 1px solid var(--color-border);
}
.chat-input textarea {
  flex: 1;
  resize: none;
  border: 1.5px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: 0.5rem 0.65rem;
  font: inherit;
  font-size: 0.88rem;
  outline: none;
  color: var(--color-text);
  background: var(--color-bg);
}
.chat-input textarea:focus {
  border-color: var(--color-accent);
}
.chat-input button {
  width: 38px;
  height: 38px;
  border: none;
  border-radius: var(--radius-md);
  background: var(--color-accent);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  transition: background 0.2s;
}
.chat-input button:hover:not(:disabled) { background: var(--c-accent-dark); }
.chat-input button:disabled { opacity: 0.4; cursor: not-allowed; }

/* Transition */
.chat-slide-enter-active,
.chat-slide-leave-active {
  transition: opacity 0.25s, transform 0.25s;
}
.chat-slide-enter-from,
.chat-slide-leave-to {
  opacity: 0;
  transform: translateY(12px) scale(0.96);
}

@media (max-width: 480px) {
  .chat-panel {
    width: calc(100vw - 2rem);
    right: 1rem;
    bottom: 5rem;
    max-height: 70vh;
  }
}
</style>
