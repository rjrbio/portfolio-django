#!/usr/bin/env python3
"""
Script para generar archivo .env con credenciales seguras
Uso: python setup_env.py
"""

import secrets
import string
from pathlib import Path

def generate_password(length=20):
    """Genera una contraseña segura"""
    characters = string.ascii_letters + string.digits + "!@#$%^&*-_+"
    return ''.join(secrets.choice(characters) for _ in range(length))

def generate_secret_key():
    """Genera una SECRET_KEY de Django"""
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return ''.join(secrets.choice(chars) for _ in range(50))

def main():
    env_file = Path('.env')
    
    if env_file.exists():
        response = input('⚠️  El archivo .env ya existe. ¿Sobrescribir? (s/N): ')
        if response.lower() != 's':
            print('❌ Operación cancelada')
            return
    
    print('🔐 Generando credenciales seguras...\n')
    
    # Solicitar datos
    username = input('👤 Nombre de usuario admin (Enter para aleatorio): ').strip()
    if not username:
        username = f"admin_{secrets.token_hex(4)}"
    
    email = input('📧 Email del admin: ').strip()
    if not email:
        email = 'admin@example.com'
    
    # Generar credenciales
    password = generate_password(20)
    secret_key = generate_secret_key()
    
    # Contenido del .env
    env_content = f"""# Variables de entorno - GENERADO AUTOMÁTICAMENTE
# NO SUBIR ESTE ARCHIVO A GIT

# Django
DEBUG=False
SECRET_KEY={secret_key}
ALLOWED_HOSTS=localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS=http://localhost,http://localhost:8080

# Superusuario Django
DJANGO_SUPERUSER_USERNAME={username}
DJANGO_SUPERUSER_EMAIL={email}
DJANGO_SUPERUSER_PASSWORD={password}

# Base de Datos PostgreSQL
DB_NAME=portfolio_db
DB_USER=portfolio_user
DB_PASSWORD=portfolio_password
DB_HOST=db
DB_PORT=5432

# Alternativa: DATABASE_URL
# DATABASE_URL=postgresql://usuario:contraseña@host:puerto/nombre_db
"""
    
    # Guardar archivo
    env_file.write_text(env_content, encoding='utf-8')
    
    print('\n✅ Archivo .env creado exitosamente!\n')
    print('📋 GUARDA ESTAS CREDENCIALES DE FORMA SEGURA:')
    print('=' * 60)
    print(f'Usuario admin: {username}')
    print(f'Email:         {email}')
    print(f'Contraseña:    {password}')
    print('=' * 60)
    print('\n⚠️  IMPORTANTE:')
    print('   1. Guarda estas credenciales en un lugar seguro')
    print('   2. El archivo .env NO se subirá a Git (está en .gitignore)')
    print('   3. Para producción, actualiza ALLOWED_HOSTS y CSRF_TRUSTED_ORIGINS')
    print('   4. Accede al admin en: http://localhost:8080/admin/\n')

if __name__ == '__main__':
    main()
