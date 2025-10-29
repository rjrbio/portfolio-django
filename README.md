# Portfolio Django

Portfolio personal moderno con diseño dark theme, desarrollado con Django 5.2 y PostgreSQL.

## ⚙️ Características

- **Aplicaciones Django**: Core, Proyectos, Servicios, Tecnologías, Testimonios, Blog, Currículum, Contacto y Sobre Mí
- **Tecnologías**: Frontend, Backend, Bases de Datos y Herramientas
- **Sistema de Blog**: Con imágenes destacadas y gestión de contenido
- **Currículum Dinámico**: Educación y experiencia laboral
- **Gestión de Proyectos**: Portafolio de trabajos con imágenes y enlaces
- **Admin Django**: Panel completo para gestionar todo el contenido
- **Dockerizado**: Deployment con Docker Compose (Django + PostgreSQL + Nginx)

## 🛠️ Stack Tecnológico

- **Backend**: Django 5.2, Python 3.12
- **Base de Datos**: PostgreSQL
- **Frontend**: HTML5, CSS3, DevIcon CDN
- **Servidor**: Gunicorn + Nginx
- **Containerización**: Docker
- **Imágenes**: Pillow para procesamiento

## 📦 Instalación

```bash
# Clonar repositorio
git clone https://github.com/rjrbio/portfolio-django.git
cd portfolio-django

# Levantar con Docker
docker-compose up -d

# Restaurar el backup (IMPORTANTE)
docker-compose exec -T db psql -U portfolio_user portfolio_db < backup.sql

# Crear superusuario
docker-compose exec web python manage.py createsuperuser

# Acceder
# Portfolio: http://localhost:8080
# Admin: http://localhost:8080/admin
```

## 🎨 Diseño

- Paleta de colores: Púrpura y Rosa 
- Efectos: Hover animations, floating elements, gradients
- Responsive design
- Favicon personalizado con iniciales <RJ/>

## 📝 Licencia

Proyecto personal de portfolio.

## 🕵️ Presentación 

