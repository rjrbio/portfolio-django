#!/usr/bin/env python
"""
Script para crear superusuario automáticamente si no existe
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Obtener credenciales de variables de entorno
username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'admin123')

# Crear superusuario si no existe
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f'✓ Superusuario "{username}" creado exitosamente')
else:
    print(f'⚠ El superusuario "{username}" ya existe')
