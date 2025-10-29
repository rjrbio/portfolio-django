#!/bin/bash
set -e

echo "🔍 Verificando migraciones..."
python manage.py showmigrations

echo "🗄️ Aplicando migraciones..."
python manage.py migrate --noinput

echo "📁 Recopilando archivos estáticos..."
python manage.py collectstatic --no-input --clear

echo "👤 Creando superusuario..."
python manage.py ensure_superuser || echo "⚠️ Superusuario ya existe o error"

echo "🚀 Iniciando Gunicorn..."
exec gunicorn --bind 0.0.0.0:8000 \
    --workers 2 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile - \
    --log-level info \
    portfolio.wsgi:application
