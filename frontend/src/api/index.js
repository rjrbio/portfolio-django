const BASE_URL = import.meta.env.VITE_API_URL || '/api/v1'
const DEFAULT_TIMEOUT_MS = 10_000
const MAX_RETRIES = 2

async function apiFetch(path, options = {}, attempt = 1) {
  // Separamos signal para que no sobrescriba el AbortController interno
  const { signal: _ignored, ...restOptions } = options
  const controller = new AbortController()
  const timeoutId = setTimeout(() => controller.abort(), DEFAULT_TIMEOUT_MS)

  try {
    const response = await fetch(`${BASE_URL}${path}`, {
      headers: { 'Content-Type': 'application/json', ...restOptions.headers },
      ...restOptions,
      signal: controller.signal,
    })
    clearTimeout(timeoutId)
    if (!response.ok) {
      const error = await response.json().catch(() => ({}))
      throw { status: response.status, data: error }
    }
    return response.json()
  } catch (err) {
    clearTimeout(timeoutId)
    if (err.name === 'AbortError') {
      throw { status: 408, data: { detail: 'La petición tardó demasiado. Inténtalo de nuevo.' } }
    }
    const isGet = !restOptions.method || restOptions.method.toUpperCase() === 'GET'
    if (isGet && attempt < MAX_RETRIES) {
      return apiFetch(path, options, attempt + 1)
    }
    throw err
  }
}

export const api = {
  home: () => apiFetch('/'),
  projects: () => apiFetch('/projects/'),
  project: (slug) => apiFetch(`/projects/${slug}/`),
  about: () => apiFetch('/about/'),
  contact: (data) => apiFetch('/contact/', { method: 'POST', body: JSON.stringify(data) }),
  services: () => apiFetch('/services/'),
  testimonials: () => apiFetch('/testimonials/'),
  techs: () => apiFetch('/techs/'),
  blog: () => apiFetch('/blog/'),
  post: (slug) => apiFetch(`/blog/${slug}/`),
  resume: () => apiFetch('/resume/'),
  agent: (question) => apiFetch('/agent/', { method: 'POST', body: JSON.stringify({ question }) }),
}
