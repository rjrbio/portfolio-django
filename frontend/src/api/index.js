const BASE_URL = import.meta.env.VITE_API_URL || '/api/v1'

async function apiFetch(path, options = {}) {
  const response = await fetch(`${BASE_URL}${path}`, {
    headers: { 'Content-Type': 'application/json', ...options.headers },
    ...options,
  })
  if (!response.ok) {
    const error = await response.json().catch(() => ({}))
    throw { status: response.status, data: error }
  }
  return response.json()
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
