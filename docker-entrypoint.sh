#!/bin/bash
set -e

echo "🔍 Verificando migraciones..."
python manage.py showmigrations

echo "🗄️ Aplicando migraciones..."
python manage.py migrate --noinput

echo "📁 Recopilando archivos estáticos..."
python manage.py collectstatic --no-input --clear

echo "👤 Creando superusuario..."
if python manage.py ensure_superuser; then
    echo "✅ Superusuario configurado correctamente"
else
    echo "❌ ERROR: No se pudo crear el superusuario"
    echo "⚠️  Verifica que las variables de entorno estén configuradas en .env"
    echo "⚠️  Ejecuta: python setup_env.py para generar credenciales seguras"
    exit 1
fi

echo "📦 Cargando datos iniciales (si existen fixtures y es el primer deploy)..."
if [ ! -f "/app/.data_loaded" ]; then
    python manage.py load_initial_data && touch /app/.data_loaded || echo "⚠️ No hay fixtures para cargar"
else
    echo "⚠️ Datos ya cargados previamente, saltando..."
fi

echo "�🚀 Iniciando Gunicorn..."
exec gunicorn --bind 0.0.0.0:8000 \
    --workers 2 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile - \
    --log-level info \
    portfolio.wsgi:application
