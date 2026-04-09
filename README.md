# Portfolio - Vue + Vite + Django REST Framework

Portfolio personal con arquitectura SPA con Vue 3 + Vite en frontend y API REST con Django REST Framework en backend.

## Arquitectura Actual

- Frontend desacoplado en Vue 3 (SPA) dentro de la carpeta frontend
- Build del frontend generado en static/vue para servirlo desde Django
- Backend API en Django 5.2 + DRF bajo el prefijo /api/v1/
- Base de datos PostgreSQL
- Servido en producción con Gunicorn + Nginx (Docker Compose)

## Stack Tecnológico

- Frontend: Vue 3, Vue Router, Pinia, Vite 8
- Backend: Django 5.2, Django REST Framework
- Base de datos: PostgreSQL 15
- Infraestructura: Docker, Docker Compose, Nginx, Gunicorn
- Otros: Pillow, django-cors-headers, WhiteNoise

## Estructura del Proyecto

- frontend/: aplicación Vue + Vite
- apps/: módulos Django (about, projects, services, techs, testimonials, blog, resume, contact, core, agent)
- portfolio/: configuración principal de Django (settings, urls, wsgi/asgi)
- templates/spa.html: shell HTML que monta la SPA compilada
- static/vue/: artefactos del build frontend servidos por Django

## Endpoints y Routing

- API: /api/v1/
- Admin: /admin/
- Health check: /health/
- Media: /media/
- Cualquier ruta no API/Admin/Media responde el shell SPA (templates/spa.html)
