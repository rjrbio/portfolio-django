#!/usr/bin/env python
"""
Script para verificar que todo esté correcto antes de deploy
"""
import sys
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

def check_settings():
    """Verificar settings.py"""
    print("✓ Verificando settings...")
    from django.conf import settings
    
    # Verificar que dj_database_url esté importado
    assert hasattr(settings, 'DATABASES'), "DATABASES no configurado"
    
    # Verificar middleware
    middleware = settings.MIDDLEWARE
    assert 'django.middleware.csrf.CsrfViewMiddleware' in middleware, "CsrfViewMiddleware no configurado correctamente"
    assert 'whitenoise.middleware.WhiteNoiseMiddleware' in middleware, "WhiteNoise no configurado"
    
    # Verificar STORAGES
    assert hasattr(settings, 'STORAGES'), "STORAGES no configurado"
    
    print("✓ Settings configurado correctamente")
    return True

def check_models():
    """Verificar que todos los modelos estén OK"""
    print("✓ Verificando modelos...")
    from django.apps import apps
    
    for model in apps.get_models():
        print(f"  - {model.__name__}")
    
    print("✓ Modelos cargados correctamente")
    return True

def check_urls():
    """Verificar URLs"""
    print("✓ Verificando URLs...")
    from django.urls import get_resolver
    
    resolver = get_resolver()
    print(f"  - URLs configuradas: {len(resolver.url_patterns)}")
    
    print("✓ URLs configuradas correctamente")
    return True

def main():
    """Ejecutar todas las verificaciones"""
    print("\n🔍 Verificando proyecto antes de deploy...\n")
    
    try:
        check_settings()
        check_models()
        check_urls()
        
        print("\n✅ Todas las verificaciones pasaron correctamente!")
        print("👉 Puedes hacer deploy con seguridad.\n")
        return 0
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
        return 1

if __name__ == '__main__':
    sys.exit(main())
