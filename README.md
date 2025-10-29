# Portfolio Django

Portfolio personal moderno con diseño dark theme, desarrollado con Django 5.2 y PostgreSQL.

## 🚀 Características

- **9 Aplicaciones Django**: Core, Proyectos, Servicios, Tecnologías, Testimonios, Blog, Currículum, Contacto y Sobre Mí
- **Diseño Moderno**: Dark theme con gradientes púrpura-rosa, glassmorphism y animaciones suaves
- **28 Tecnologías**: Frontend, Backend, Bases de Datos y Herramientas con iconos DevIcon
- **Sistema de Blog**: Con imágenes destacadas y gestión de contenido
- **Currículum Dinámico**: Educación y experiencia laboral
- **Gestión de Proyectos**: Portafolio de trabajos con imágenes y enlaces
- **Contacto**: Formulario funcional con validación
- **Admin Django**: Panel completo para gestionar todo el contenido
- **Dockerizado**: Deployment con Docker Compose (Django + PostgreSQL + Nginx)

## 🛠️ Stack Tecnológico

- **Backend**: Django 5.2.7, Python 3.12
- **Base de Datos**: PostgreSQL 15
- **Frontend**: HTML5, CSS3 (animaciones custom), DevIcon CDN
- **Servidor**: Gunicorn + Nginx
- **Containerización**: Docker & Docker Compose
- **Imágenes**: Pillow para procesamiento

## 📦 Instalación

```bash
# Clonar repositorio
git clone https://github.com/rjrbio/portfolio-django.git
cd portfolio-django

# Levantar con Docker
docker-compose up -d

# Crear superusuario
docker-compose exec web python manage.py createsuperuser

# Acceder
# Portfolio: http://localhost:8080
# Admin: http://localhost:8080/admin
```

## 🎨 Diseño

- Paleta de colores: Púrpura (#a855f7) y Rosa (#ec4899)
- Efectos: Hover animations, floating elements, gradients
- Responsive design
- Favicon personalizado con iniciales <RJ/>

## 📝 Licencia

Proyecto personal de portfolio.
