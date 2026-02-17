# ⚡ QUICK REFERENCE - Comandos y Configuración

Referencia rápida de comandos frecuentes.

## 🚀 Setup Rápido

### Local con Docker (30 segundos)
```bash
docker-compose up -d
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
# Abre: http://localhost:8080
```

### Local sin Docker (1 minuto)
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edita .env con tu BD local
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver  # http://localhost:8000
```

### AlwaysData (20 minutos)
```bash
# En consola AlwaysData:
pip install -r requirements.txt

cat > .env << 'EOF'
DEBUG=False
SECRET_KEY=valor-largo-aleatorio
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
# Configura WSGI: portfolio.wsgi:application
```

---

## 📦 Dependencias

### Instalar TODAS
```bash
pip install -r requirements.txt
```

### Instalar UNA NUEVA
```bash
pip install nombre-paquete
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Add: nombre-paquete"
```

### Actualizar EXISTENTE
```bash
pip install --upgrade nombre-paquete
pip freeze > requirements.txt
```

---

## 🗄️ Base de Datos

### Migraciones
```bash
# Crear migraciones (después de cambiar models.py)
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Ver estado
python manage.py showmigrations

# Deshacer última
python manage.py migrate app_name 0001
```

### Conexión Directa
```bash
# Acceder a la BD directa
python manage.py dbshell

# En la consola PostgreSQL:
\dt                    # Listar tablas
\du                    # Listar usuarios
SELECT * FROM app_table;  # Ver datos
```

### Backup / Restore
```bash
# Backup
python manage.py dumpdata > backup.json

# Restore
python manage.py loaddata backup.json
```

---

## 👤 Admin y Usuarios

### Crear Superusuario
```bash
python manage.py createsuperuser
```

### Crear Usuario Regular
```bash
python manage.py shell
```
```python
from django.contrib.auth.models import User
User.objects.create_user(username='usuario', password='pass')
```

### Ver Admin
```bash
# Abrir navegador
http://localhost:8000/admin  # Local
https://tu-dominio.alwaysdata.net/admin  # Producción
```

---

## 📁 Archivos Estáticos y Media

### Recopilar Estáticos (después de cambios CSS/JS)
```bash
python manage.py collectstatic --noinput
# Copia static/ → staticfiles/
```

### Limpiar Estáticos
```bash
python manage.py collectstatic --clear --noinput
```

### Ver Información
```bash
python manage.py findstatic nombre-archivo.css
```

---

## 🔧 Variables de Entorno

### Ver Variables Actuales
```bash
# En Python
python manage.py shell
```
```python
import os
print(os.getenv("DEBUG"))
print(os.getenv("ALLOWED_HOSTS"))
```

### En Linux/Mac
```bash
env | grep DB_      # Ver todas DB_*
env | grep DJANGO   # Ver todas DJANGO*
```

### En Windows PowerShell
```powershell
Get-ChildItem Env:DB_*
Get-ChildItem Env:ALLOWED_HOSTS
```

---

## 🐛 Debugging

### Ver Errores
```bash
# Nivel INFO
python manage.py runserver --verbosity 3

# Logs del proyecto
cat logs/django.log
```

### Shell Interactivo
```bash
python manage.py shell
```
```python
from apps.projects.models import Project
Project.objects.all()
Project.objects.filter(featured=True)
Project.objects.get(id=1)
```

### Tests
```bash
# Correr todos
python manage.py test

# Correr una app
python manage.py test apps.projects

# Correr un test
python manage.py test apps.projects.tests.ProjectTests
```

---

## 📤 Deploy

### A AlwaysData
```bash
# 1. Push a GitHub
git add .
git commit -m "cambios"
git push

# 2. En AlwaysData console:
cd /home/usuario/www/portfolio-django
git pull

# 3. Ejecutar:
python manage.py migrate --noinput
python manage.py collectstatic --noinput

# 4. Reiniciar app en panel
```

### A Render (si tienes DATABASE_URL)
```bash
# Automático con push a GitHub
git push  # Deploy automático en Render
```

### A Docker
```bash
docker-compose up -d       # Iniciar
docker-compose down        # Detener
docker-compose logs -f web # Ver logs
docker-compose exec web bash  # Entrar a contenedor
```

---

## 🔐 Seguridad

### Generar SECRET_KEY Nuevo
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Verificar Seguridad
```bash
python manage.py check --deploy

# Buscar secretos en código
grep -r "password" --include="*.py"
grep -r "secret" --include="*.py"
```

### HTTPS Check
```bash
# En settings.py:
# SECURE_SSL_REDIRECT = True (ya configurado si DEBUG=False)
```

---

## 📚 Git

### Antes de Hacer Commit
```bash
# Ver cambios
git status
git diff

# IMPORTANTE: .env NO debe estar
git status | grep .env  # Debe estar en rojo (ignored)
```

### Workflow Típico
```bash
# Crear rama
git checkout -b feature/nombre

# Cambios
git add .
git commit -m "feat: descripción"

# Push
git push origin feature/nombre

# Pull Request (GitHub)
# Merge en main
```

### Ver Historial
```bash
git log --oneline        # Últimos commits
git log --oneline -n 10  # Últimos 10
git diff HEAD~2          # Cambios últimas 2 commits
```

---

## 🚨 Errores Comunes

| Error | Solución |
|-------|----------|
| `ModuleNotFoundError: No module named 'django'` | `pip install -r requirements.txt` |
| `Couldn't import Django` | `source venv/bin/activate` |
| `could not translate host name` | Verifica `DB_HOST` en `.env` |
| `ALLOWED_HOSTS` error | Añade dominio a `.env`: `ALLOWED_HOSTS=tu-dominio.com` |
| `Table does not exist` | `python manage.py migrate` |
| `Static files not found` | `python manage.py collectstatic` |
| `Media files not found` | Verifica carpeta `media/` permissions |
| `Admin no funciona` | `python manage.py createsuperuser` |

---

## 🎯 URLs Frecuentes

```
Local:
- Sitio: http://localhost:8080 (Docker) o http://localhost:8000 (runserver)
- Admin: http://localhost:8080/admin (Docker) o http://localhost:8000/admin

AlwaysData:
- Sitio: https://tu-usuario.alwaysdata.net
- Admin: https://tu-usuario.alwaysdata.net/admin

Render:
- Sitio: https://tu-app.onrender.com
- Admin: https://tu-app.onrender.com/admin
```

---

## 📞 Ayuda Rápida

```bash
# Ver todas las opciones de manage.py
python manage.py help

# Ver ayuda de un comando específico
python manage.py help migrate

# Ver stats del proyecto
find apps -name "*.py" -type f | wc -l  # Archivos Python
find templates -name "*.html" | wc -l   # Templates
```

---

## ✨ Tips Pro

1. **Guardar búsqueda frecuentes** en shell
```bash
# Crea archivo: ~/.bash_profile o ~/.zshrc
alias rundjango="python manage.py runserver"
alias pmigrate="python manage.py migrate"
```

2. **Usar .env para variaciones locales**
```bash
# .env.dev vs .env.prod (no commitear)
source .env.prod && python manage.py migrate
```

3. **Alias para comandos largos**
```python
# En manage.py:
# Crea custom commands en apps/app/management/commands/
```

4. **Usar pdb para debug**
```python
# En el código:
import pdb; pdb.set_trace()  # Pausa ejecución
```

5. **Watch tests automáticos**
```bash
pip install pytest-watch
ptw  # Corre tests automáticamente cuando editas
```

---

## 📋 Checklist Pre-Commit

- [ ] `git status` veo cambios esperados
- [ ] `.env` está en rojo (ignored)
- [ ] No hay archivos `.pyc` o `__pycache__`
- [ ] `python manage.py test` pasa
- [ ] `python manage.py check --deploy` OK
- [ ] Commit message descriptivo
- [ ] `git push` y verificar en GitHub

---

**Referencia rápida v1.0 - 17 Feb 2026**

Para más info: [INDEX.md](INDEX.md)
