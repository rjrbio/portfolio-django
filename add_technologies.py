"""
Script para agregar tecnologías comunes al portfolio
"""
from apps.techs.models import Technology

# Eliminar tecnologías existentes si quieres empezar de cero
# Technology.objects.all().delete()

# Lista de tecnologías comunes
technologies = [
    # Frontend
    {"name": "HTML5", "category": "Frontend", "proficiency": 90},
    {"name": "CSS3", "category": "Frontend", "proficiency": 85},
    {"name": "JavaScript", "category": "Frontend", "proficiency": 80},
    {"name": "React", "category": "Frontend", "proficiency": 75},
    {"name": "Vue.js", "category": "Frontend", "proficiency": 70},
    {"name": "Bootstrap", "category": "Frontend", "proficiency": 85},
    {"name": "Tailwind CSS", "category": "Frontend", "proficiency": 80},
    
    # Backend
    {"name": "Python", "category": "Backend", "proficiency": 85},
    {"name": "Django", "category": "Backend", "proficiency": 80},
    {"name": "Flask", "category": "Backend", "proficiency": 75},
    {"name": "PHP", "category": "Backend", "proficiency": 70},
    {"name": "Node.js", "category": "Backend", "proficiency": 75},
    {"name": "Express.js", "category": "Backend", "proficiency": 70},
    
    # Bases de datos
    {"name": "MySQL", "category": "Base de datos", "proficiency": 80},
    {"name": "PostgreSQL", "category": "Base de datos", "proficiency": 85},
    {"name": "MongoDB", "category": "Base de datos", "proficiency": 70},
    {"name": "SQLite", "category": "Base de datos", "proficiency": 75},
    {"name": "Redis", "category": "Base de datos", "proficiency": 65},
    
    # DevOps y herramientas
    {"name": "Git", "category": "DevOps", "proficiency": 85},
    {"name": "GitHub", "category": "DevOps", "proficiency": 85},
    {"name": "Docker", "category": "DevOps", "proficiency": 75},
    {"name": "Linux", "category": "DevOps", "proficiency": 80},
    {"name": "Nginx", "category": "DevOps", "proficiency": 70},
    
    # Otros
    {"name": "REST API", "category": "Arquitectura", "proficiency": 80},
    {"name": "GraphQL", "category": "Arquitectura", "proficiency": 65},
]

# Crear las tecnologías
created_count = 0
for tech_data in technologies:
    tech, created = Technology.objects.get_or_create(
        name=tech_data["name"],
        defaults={
            "category": tech_data["category"],
            "proficiency": tech_data["proficiency"]
        }
    )
    if created:
        created_count += 1
        print(f"✓ Creada: {tech.name} ({tech.category}) - {tech.proficiency}%")
    else:
        print(f"- Ya existe: {tech.name}")

print(f"\n✅ Proceso completado: {created_count} tecnologías creadas")
print(f"📊 Total de tecnologías en la base de datos: {Technology.objects.count()}")
