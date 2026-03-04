#!/usr/bin/env python
"""
Script de limpieza de usuarios inseguros para AlwaysData/SSH
Ejecutar: python cleanup_admin.py
"""

import os
import sys
import django

# Configurar Django
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

print("\n" + "="*60)
print("🔒 LIMPIEZA DE USUARIOS INSEGUROS")
print("="*60 + "\n")

# Buscar usuario 'admin' con password inseguro
admin_user = User.objects.filter(username='admin').first()

if admin_user:
    print(f"✓ Usuario 'admin' encontrado")
    print(f"  Email: {admin_user.email}")
    print(f"  Es superusuario: {admin_user.is_superuser}")
    print(f"  Creado: {admin_user.date_joined}\n")
    
    # Verificar si tiene password inseguro
    if admin_user.check_password('admin123'):
        print("❌ ¡¡PELIGRO!! El usuario 'admin' tiene password: admin123")
        print("\n🔒 Eliminando usuario 'admin' inseguro...\n")
        admin_user.delete()
        print("✅ Usuario 'admin' ELIMINADO correctamente")
    elif admin_user.check_password('admin'):
        print("❌ ¡¡PELIGRO!! El usuario 'admin' tiene password: admin")
        print("\n🔒 Eliminando usuario 'admin' inseguro...\n")
        admin_user.delete()
        print("✅ Usuario 'admin' ELIMINADO correctamente")
    else:
        print("ℹ️  El usuario 'admin' existe pero tiene otro password")
        print("   (No se elimina por seguridad)")
else:
    print("✅ No existe usuario 'admin' inseguro\n")

# Verificar otros usuarios inseguros
insecure_usernames = ['administrator', 'root', 'test', 'demo']
for username in insecure_usernames:
    user = User.objects.filter(username=username).first()
    if user:
        print(f"⚠️  Usuario '{username}' encontrado - verificando...")
        if user.check_password('admin123') or user.check_password('password') or user.check_password('123456'):
            print(f"   ❌ Tiene password inseguro - ELIMINANDO...")
            user.delete()
            print(f"   ✅ Usuario '{username}' eliminado")

# Listar usuarios finales
print("\n" + "="*60)
print("USUARIOS FINALES EN LA BASE DE DATOS:")
print("="*60 + "\n")

for user in User.objects.all():
    superuser_text = "👑 SUPERUSUARIO" if user.is_superuser else "usuario regular"
    print(f"  • {user.username:20} - {user.email:30} - {superuser_text}")

print("\n" + "="*60)
print("✅ LIMPIEZA COMPLETADA")
print("="*60 + "\n")
