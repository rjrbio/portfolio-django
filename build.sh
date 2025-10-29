#!/usr/bin/env bash
set -o errexit

echo "📦 Instalando dependencias..."
pip install -r requirements.txt

echo "📁 Recopilando archivos estáticos..."
python manage.py collectstatic --no-input --clear

echo "🗄️ Aplicando migraciones..."
python manage.py migrate --noinput

echo "👤 Creando superusuario..."
python manage.py ensure_superuser || echo "⚠️ No se pudo crear el superusuario (puede que ya exista)"

echo "✅ Build completado exitosamente"