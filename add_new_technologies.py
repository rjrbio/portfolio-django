"""
Script para agregar Angular, Markdown y Java a las tecnologías
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from apps.techs.models import Technology

# Nuevas tecnologías a agregar
new_technologies = [
    {
        'name': 'Angular',
        'icon_class': 'devicon-angularjs-plain colored',
        'proficiency': 75,
        'category': 'frontend',
    },
    {
        'name': 'Markdown',
        'icon_class': 'devicon-markdown-original',
        'proficiency': 90,
        'category': 'other',
    },
    {
        'name': 'Java',
        'icon_class': 'devicon-java-plain colored',
        'proficiency': 80,
        'category': 'backend',
    },
]

# Agregar las tecnologías
added_count = 0
for tech_data in new_technologies:
    tech, created = Technology.objects.get_or_create(
        name=tech_data['name'],
        defaults={
            'icon_class': tech_data['icon_class'],
            'proficiency': tech_data['proficiency'],
            'category': tech_data['category'],
        }
    )
    
    if created:
        print(f"✓ {tech.name} agregado - {tech.get_category_display()} ({tech.proficiency}%)")
        added_count += 1
    else:
        print(f"⚠ {tech.name} ya existe")

print(f"\n✅ {added_count} tecnología(s) nueva(s) agregada(s)")
print(f"📊 Total de tecnologías: {Technology.objects.count()}")
