#!/usr/bin/env bash
set -o errexit

echo "📦 Instalando dependencias..."
pip install -r requirements.txt

echo "� Verificando migraciones..."
python manage.py showmigrations

echo "🗄️ Creando/Aplicando migraciones..."
python manage.py makemigrations --noinput || echo "⚠️ No hay nuevas migraciones"
python manage.py migrate --noinput

echo "� Recopilando archivos estáticos..."
python manage.py collectstatic --no-input --clear

echo "👤 Creando superusuario..."
python manage.py ensure_superuser || echo "⚠️ No se pudo crear el superusuario (puede que ya exista)"

echo "✅ Build completado exitosamente"