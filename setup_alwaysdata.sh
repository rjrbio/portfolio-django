#!/bin/bash

# Script de instalación para AlwaysData
# Este script configura la aplicación en AlwaysData de forma segura

echo "🚀 INSTALACIÓN Y CONFIGURACIÓN SEGURA EN ALWAYSDATA"
echo "=================================================="

# 1. Cargar variables de entorno
export DJANGO_SETTINGS_MODULE=portfolio.settings

echo ""
echo "1️⃣  Verificando variables de entorno (.env)..."
if [ ! -f ".env" ]; then
    echo "❌ El archivo .env NO existe"
    echo "📝 Crea .env con las siguientes variables:"
    echo ""
    echo "DEBUG=False"
    echo "SECRET_KEY=tu-clave-secreta"
    echo "ALLOWED_HOSTS=tu-dominio.com"
    echo "DJANGO_SUPERUSER_USERNAME=tu_usuario"
    echo "DJANGO_SUPERUSER_EMAIL=tu_email@dominio.com"
    echo "DJANGO_SUPERUSER_PASSWORD=tu_password_seguro"
    echo "DB_NAME=portfolio_db"
    echo "DB_USER=portfolio_user"
    echo "DB_PASSWORD=tu_password_db"
    echo "DB_HOST=postgresql-host.alwaysdata.net"
    echo "DB_PORT=5432"
    echo ""
    exit 1
else
    echo "✅ Archivo .env encontrado"
fi

# 2. Ejecutar migraciones
echo ""
echo "2️⃣  Ejecutando migraciones..."
python manage.py migrate --noinput
if [ $? -eq 0 ]; then
    echo "✅ Migraciones completadas"
else
    echo "❌ Error en migraciones"
    exit 1
fi

# 3. Limpiar usuarios inseguros
echo ""
echo "3️⃣  Limpiando usuarios inseguros..."
python cleanup_admin.py
if [ $? -eq 0 ]; then
    echo "✅ Limpieza de usuarios completada"
else
    echo "❌ Error al limpiar usuarios (revisa .env)"
fi

# 4. Crear superusuario
echo ""
echo "4️⃣  Creando/verificando superusuario seguro..."
python manage.py ensure_superuser
if [ $? -eq 0 ]; then
    echo "✅ Superusuario configurado"
else
    echo "❌ Error al crear superusuario"
    exit 1
fi

# 5. Staticfiles
echo ""
echo "5️⃣  Recopilando archivos estáticos..."
python manage.py collectstatic --noinput --clear
if [ $? -eq 0 ]; then
    echo "✅ Archivos estáticos recopilados"
fi

echo ""
echo "=================================================="
echo "✅ INSTALACIÓN COMPLETADA"
echo "=================================================="
echo ""
echo "📌 Próximos pasos:"
echo "1. Accede a https://tu-dominio.com/admin/"
echo "2. Login con el usuario configurado en .env"
echo "3. Verifica que el usuario 'admin' NO existe"
echo ""
