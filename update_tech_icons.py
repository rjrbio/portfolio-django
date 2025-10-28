"""
Script para actualizar las tecnologías con iconos de DevIcon
"""
from apps.techs.models import Technology

# Mapeo de tecnologías a sus clases de iconos DevIcon
tech_icons = {
    # Frontend
    "HTML5": "devicon-html5-plain colored",
    "CSS3": "devicon-css3-plain colored",
    "JavaScript": "devicon-javascript-plain colored",
    "React": "devicon-react-original colored",
    "Vue.js": "devicon-vuejs-plain colored",
    "Bootstrap": "devicon-bootstrap-plain colored",
    "Tailwind CSS": "devicon-tailwindcss-plain colored",
    
    # Backend
    "Python": "devicon-python-plain colored",
    "Django": "devicon-django-plain colored",
    "Flask": "devicon-flask-original colored",
    "PHP": "devicon-php-plain colored",
    "Node.js": "devicon-nodejs-plain colored",
    "Express.js": "devicon-express-original colored",
    
    # Bases de datos
    "MySQL": "devicon-mysql-plain colored",
    "PostgreSQL": "devicon-postgresql-plain colored",
    "MongoDB": "devicon-mongodb-plain colored",
    "SQLite": "devicon-sqlite-plain colored",
    "Redis": "devicon-redis-plain colored",
    
    # DevOps
    "Git": "devicon-git-plain colored",
    "GitHub": "devicon-github-original colored",
    "Docker": "devicon-docker-plain colored",
    "Linux": "devicon-linux-plain colored",
    "Nginx": "devicon-nginx-original colored",
}

# Mapeo de categorías antiguas a nuevas
category_map = {
    "Frontend": "frontend",
    "Backend": "backend",
    "Base de datos": "database",
    "DevOps": "tools",
    "Arquitectura": "other",
}

updated_count = 0
for tech in Technology.objects.all():
    # Actualizar icono si existe en el mapeo
    if tech.name in tech_icons:
        tech.icon_class = tech_icons[tech.name]
        updated_count += 1
        print(f"✓ Actualizado: {tech.name} -> {tech.icon_class}")
    
    # Actualizar categoría al nuevo formato
    if tech.category in category_map:
        old_category = tech.category
        tech.category = category_map[tech.category]
        print(f"  📁 Categoría: {old_category} -> {tech.category}")
    
    tech.save()

print(f"\n✅ Actualización completada: {updated_count} tecnologías con iconos")
print(f"📊 Total de tecnologías: {Technology.objects.count()}")

# Mostrar estadísticas por categoría
print("\n📊 Tecnologías por categoría:")
for category_code, category_name in [('frontend', 'Frontend'), ('backend', 'Backend'), 
                                      ('database', 'Base de Datos'), ('tools', 'Herramientas'), 
                                      ('other', 'Otros')]:
    count = Technology.objects.filter(category=category_code).count()
    print(f"  {category_name}: {count}")
