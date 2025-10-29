#!/usr/bin/env python
"""
Script para exportar todos los datos a fixtures JSON
"""
import os
import subprocess

# Crear carpeta fixtures si no existe
os.makedirs('fixtures', exist_ok=True)

# Lista de apps y modelos a exportar
exports = [
    ('apps.about', 'about.json'),
    ('apps.techs', 'techs.json'),
    ('apps.services', 'services.json'),
    ('apps.projects', 'projects.json'),
    ('apps.blog', 'blog.json'),
    ('apps.testimonials', 'testimonials.json'),
    ('apps.resume', 'resume.json'),
    ('apps.contact', 'contact.json'),
]

print("📦 Exportando datos a fixtures...\n")

for app, filename in exports:
    filepath = f'fixtures/{filename}'
    print(f"  ⏳ Exportando {app}...")
    
    try:
        result = subprocess.run(
            ['python', 'manage.py', 'dumpdata', app, '--indent', '2', '--output', filepath],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            # Verificar si el archivo tiene datos
            if os.path.getsize(filepath) > 10:
                print(f"  ✓ {filename} creado ({os.path.getsize(filepath)} bytes)")
            else:
                print(f"  ⚠ {filename} está vacío")
        else:
            print(f"  ✗ Error: {result.stderr}")
    except Exception as e:
        print(f"  ✗ Error: {e}")

print("\n✅ Exportación completada!")
print("\n💡 Ahora puedes:")
print("  1. Hacer commit de la carpeta fixtures/")
print("  2. Subir a GitHub")
print("  3. En Render, correr: python manage.py load_initial_data")
