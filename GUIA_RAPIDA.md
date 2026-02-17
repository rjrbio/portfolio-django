# 🚀 Guía Rápida para Desarrolladores

Para que otros desarrolladores no pierdan tiempo configurando.

## 🔌 Configuración Rápida (5 minutos)

### Opción A: Desarrollo Local con Docker
```bash
cp .env.example .env
# Edita .env con valores locales (o deja defaults)
docker-compose up -d
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
# Abre: http://localhost:8080
```

### Opción B: Desarrollo Local sin Docker
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# Edita .env con base de datos local (localhost)

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
# Abre: http://localhost:8000
```

### Opción C: Producción en AlwaysData
```bash
# En AlwaysData console:
git clone https://github.com/rjrbio/portfolio-django.git
cd portfolio-django
pip install -r requirements.txt

# Crea .env con datos desde AlwaysData panel
cat > .env << 'EOF'
DEBUG=False
SECRET_KEY=...
DB_NAME=tu_db
DB_USER=tu_user
DB_PASSWORD=tu_pass
DB_HOST=postgresql-user.alwaysdata.net
DB_PORT=5432
ALLOWED_HOSTS=tu-dominio.alwaysdata.net
CSRF_TRUSTED_ORIGINS=https://tu-dominio.alwaysdata.net
EOF

python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py createsuperuser
# Configura WSGI → portfolio.wsgi:application
# Reinicia app
```

---

## 📂 Estructura Importante

```
portfolio-django/
├── .env                  ← LOCAL (nunca en GitHub)
├── .env.example          ← TEMPLATE (en GitHub)
├── requirements.txt      ← Dependencias pip
├── manage.py             ← CLI Django
│
├── portfolio/            ← Configuración Django
│   ├── settings.py       ← ⭐ VER AQUÍ para .env
│   ├── wsgi.py           ← Entry point
│   └── urls.py
│
├── apps/                 ← Apps Django
│   ├── core/
│   ├── projects/
│   ├── blog/
│   └── ...
│
├── templates/            ← HTML
├── static/               ← CSS/JS
└── media/                ← Imágenes de usuarios
```

---

## 🔍 Dónde Cambiar Cosas

| Tarea | Archivo |
|-------|---------|
| Añadir variable env | `.env` local + código |
| Base de datos | `.env` (DB_*) |
| URL rutas | `apps/*/urls.py` + `portfolio/urls.py` |
| Templates | `templates/` |
| Admin Django | `apps/*/admin.py` |
| Modelos datos | `apps/*/models.py` |
| Archivos estáticos | `static/` |
| Imágenes usuarios | `media/` |

---

## ✅ Antes de Hacer Commit

```bash
# 1. SIN NUNCA subir .env
git status | grep .env  # Debe estar en rojo (ignored)

# 2. Verifica que no hay credenciales en el código
grep -r "password" --include="*.py"  # No debe haber hardcodeado

# 3. Tests (si existen)
python manage.py test

# 4. Migraciones
python manage.py makemigrations
python manage.py migrate

# 5. Estáticos
python manage.py collectstatic --noinput

# 6. Commit
git add .
git commit -m "tu mensaje"
git push
```

---

## 🐛 Debugging Típicos

### "Couldn't import Django"
```bash
pip install -r requirements.txt
# o
source venv/bin/activate
```

### "could not translate host name"
```bash
# Verifica .env existe y tiene DB_HOST correcto
cat .env | grep DB_HOST
```

### "Static files not found"
```bash
python manage.py collectstatic --noinput
# En producción: nginx sirve staticfiles/
```

### "Images not loading"
```bash
# En desarrollo: collectstatic
# En producción: verifica MEDIA_ROOT permisos
ls -la media/
```

### "Admin no me deja entrar"
```bash
# Crea superusuario
python manage.py createsuperuser
```

---

## 🔐 Seguridad Checklist

- [ ] `.env` está en `.gitignore`
- [ ] No hay contraseñas hardcodeadas en código
- [ ] `DEBUG=False` en producción
- [ ] `SECRET_KEY` es aleatoria y larga
- [ ] `ALLOWED_HOSTS` está configurado
- [ ] `CSRF_TRUSTED_ORIGINS` solo tienen tus dominios

---

## 📚 Más Info

- **Instalación completa**: [DEPLOY_ALWAYSDATA.md](DEPLOY_ALWAYSDATA.md)
- **Cambios técnicos**: [MIGRACION_RESUMEN.md](MIGRACION_RESUMEN.md)
- **Verificación**: [CHECKLIST.md](CHECKLIST.md)
- **Hostings disponibles**: [HOSTINGS_MATRIX.md](HOSTINGS_MATRIX.md)

---

## 💬 Preguntas Frecuentes

**¿Cómo cambio la base de datos?**
- Edita `.env`: `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`
- Reinicia: `python manage.py migrate`

**¿Cómo añado una app Django?**
```bash
python manage.py startapp nombre_app
# Edita apps/nombre_app/models.py
# Edita apps/nombre_app/views.py
# Edita apps/nombre_app/urls.py
# Agrega a INSTALLED_APPS en settings.py
# python manage.py makemigrations
# python manage.py migrate
```

**¿Cómo hago deploy?**
- AlwaysData: [DEPLOY_ALWAYSDATA.md](DEPLOY_ALWAYSDATA.md)
- Docker: `docker-compose up -d`
- Render: Push a GitHub (automático si está configurado)

**¿Cómo vuelvo a Render?**
- Crea `DATABASE_URL` en Render
- Settings.py lo lee automáticamente
- Git push y redeploy

---

**¡Bienvenido! Feliz coding! 🚀**
