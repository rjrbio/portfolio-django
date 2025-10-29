# Portfolio Django

Portfolio personal desarrollado con Django 5.2 y PostgreSQL.

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
- Efectos: Hover animations, floating elements, gradientes
- Diseño responsivo
- Favicon personalizado

## 📝 Licencia

Proyecto personal de portfolio.

## 🕵️ Presentación 

<img width="800"  alt="image" src="https://github.com/user-attachments/assets/2ddfcb37-b1cf-4098-a8d0-c3341b74d265" />

Distintas secciones, como 
### "Sobre Mí":

<img width="800" alt="image" src="https://github.com/user-attachments/assets/a3034743-63c9-4fa5-9922-624714d06c37" />

### Proyectos: 

<img width="800" alt="image" src="https://github.com/user-attachments/assets/02981a31-114b-4a0d-b108-d6dae667c17b" />

### Blog:

<img width="800" alt="image" src="https://github.com/user-attachments/assets/de6072a6-db5d-4cff-8128-3509958c532e" />

### Currículum:

<img width="800" alt="image" src="https://github.com/user-attachments/assets/4b3cad32-bc63-44ff-b568-14aea4c6bc3b" />

Y 
### Contacto:

<img width="800" alt="image" src="https://github.com/user-attachments/assets/f81ae6cb-42ff-48b3-843f-876b939376fd" />

## 🩺 Ejemplos de cómo funciona Django:
1. Herencias de plantillas
   
    Base template
   ```
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <title>{% block title %}Portfolio{% endblock %}</title>
        <link rel="stylesheet" href="{% static 'css/style.css' %}">
    </head>
    <body>
        {% include 'partials/navbar.html' %}
        
        <main>
            {% block content %}{% endblock %}
        </main>
        
        {% include 'partials/footer.html' %}
    </body>
    </html>
    ```
    Template hijo
    ``` 
    {% extends 'base.html' %}
    {% load static %}
    
    {% block title %}Inicio - Portfolio{% endblock %}
    
    {% block content %}
    <section class="hero">
        <h1>¡Hola! Soy Jose F. Tinoco</h1>
        <p>Desarrollador Web</p>
    </section>
    {% endblock %}
    ```
2. Definición de Rutas
   
   URLs principales
   ```
   from django.contrib import admin
   from django.urls import path, include
   from django.conf import settings
   from django.conf.urls.static import static
    
   urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('apps.core.urls')),
        path('projects/', include('apps.projects.urls')),
        path('blog/', include('apps.blog.urls')),
        path('about/', include('apps.about.urls')),
    ]
    
    # Servir archivos media en desarrollo
    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```
   URLs de una app
   ```
   from django.urls import path
   from . import views
    
   app_name = 'projects'
    
   urlpatterns = [
        path('', views.project_list, name='list'),
        path('<slug:slug>/', views.project_detail, name='detail'),
    ]
   ```
3. Modelos
   
   ```Deficinión de modelo
   from django.db import models

   class Project(models.Model):
        title = models.CharField(max_length=200)
        slug = models.SlugField(unique=True)
        description = models.TextField()
        image = models.ImageField(upload_to='projects/', blank=True, null=True)
        technologies = models.CharField(max_length=200)
        created_at = models.DateTimeField(auto_now_add=True)
        featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies.split(',')]
   ```
4. Vistas (views)
   
   Vista simple
   ```
   from django.shortcuts import render
   from apps.projects.models import Project
   from apps.blog.models import Post
    
   def home(request):
       featured_projects = Project.objects.filter(featured=True)[:3]
       recent_posts = Post.objects.filter(published=True)[:3]
        
   context = {
        'featured_projects': featured_projects,
        'recent_posts': recent_posts,
    }
    return render(request, 'core/home.html', context)
   ```
   Vista con detalle
   ```
   from django.shortcuts import render, get_object_or_404

   def post_detail(request, slug):
       post = get_object_or_404(Post, slug=slug, published=True)
       return render(request, 'blog/detail.html', {'post': post})
    ```
5. Archivos estáticos
   
   Carga de archivos static (en templates)
   ```
   {% load static %}

    <!-- CSS -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    
    <!-- Imágenes -->
    <img src="{% static 'images/logo.png' %}" alt="Logo">
    
    <!-- JavaScript -->
    <script src="{% static 'js/main.js' %}"></script>
   ```
## 🔁 ACTUALIZACIÓN
Por motivos académicos he modificado parámetros para poder hacer un deploy en Render, así como obtener una base de datos persistente (usando la del propio Render).
<br>Por lo que ahora no podrá usarse de forma local -levantando contenedores con Docker- ya que la configuración para ello ya no está disponible. Sin embargo, dejo los archivos (ya obsoletos) de configuración de Docker para su inspección.
<br>Archivos importantes añadidos para la correcta funcionalidad de Render: 

```bash
render.yaml
# Configuración de Render, levanta servicios y base de datos
docker-entrypoint.sh
# Script de inicio (migraciones, collectstatic, superusuario)
.dockerignore
# Optimización del build
```
