# Resumen de Reestructuración para AlwaysData

## 📝 Cambios Realizados

Este documento resume los cambios hechos al proyecto para migrarlo de **Render** a **AlwaysData**.

### 1. **Configuración de Base de Datos (settings.py)**

**Antes (Solo Render):**
- Usaba `DATABASE_URL` automaticamente desde Render
- Defaulteaba a configuración Docker local

**Después (Render + AlwaysData):**
- Soporta `DATABASE_URL` (Render, Heroku, etc.)
- Soporta variables individuales: `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `DB_SSLMODE`
- Permite definir credenciales de AlwaysData sin URL única
- Mantiene fallback a Docker para desarrollo local

```python
# Ahora soporta ambas formas:
if os.getenv("DATABASE_URL"):
    # Render, Heroku, etc.
    DATABASES = { "default": dj_database_url.config(...) }
else:
    # AlwaysData, hostings tradicionales
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    # ... etc
```

### 2. **Variables de Entorno Seguras (settings.py)**

- **ALLOWED_HOSTS**: Defaultea a `localhost,127.0.0.1` (más seguro)
- **CSRF_TRUSTED_ORIGINS**: Defaultea a localhost (requiere configuración en producción)
- Función `get_env_list()` para parsear variables separadas por comas

```python
ALLOWED_HOSTS = get_env_list("ALLOWED_HOSTS", "localhost,127.0.0.1")
CSRF_TRUSTED_ORIGINS = get_env_list("CSRF_TRUSTED_ORIGINS", "...")
```

### 3. **Carga de .env (settings.py)**

- Ya cargaba `python-dotenv` pero sin ruta explícita
- Ahora especifica ruta exacta relativa a `BASE_DIR`
- Verifica que el archivo existe antes de cargarlo

```python
env_file = BASE_DIR / ".env"
if env_file.exists():
    load_dotenv(str(env_file))
```

### 4. **Archivos Nuevos**

#### `.env`
- Archivo local con credenciales de BD de **AlwaysData**
- **NO se sube a GitHub** (está en `.gitignore`)
- Se crea directamente en el servidor AlwaysData

#### `.env.example`
- Template con variables requeridas
- Guía para otros desarrolladores
- Se sube a GitHub (sin valores sensibles)

#### `DEPLOY_ALWAYSDATA.md`
- Guía paso a paso del deploy en AlwaysData
- Instrucciones para crear BD PostgreSQL
- Configuración WSGI
- Troubleshooting

### 5. **Documentación (README.md)**

**Cambios:**
- Añadida sección "Deploy en AlwaysData"
- Removidas instrucciones específicas de Render (mantenidas compatible)
- Documentadas variables de entorno soportadas
- Clarificado que `.env` no se sube a GitHub

### 6. **Compatibilidad Mantenida**

✅ **Sigue funcionando:**
- Docker local (`docker-compose up -d`)
- Render.yaml (si quieres volver a Render)
- Heroku con `DATABASE_URL`
- Otros hostings con variables individuales

❌ **No se tocó:**
- Dockerfiles (sirven para desarrollo/Render)
- `render.yaml` (mantiene compatibilidad con Render)
- Estructura de apps Django
- Templates y static files

### 7. **Estructura Final del Proyecto**

```
portfolio-django/
├── .env                      ← Credenciales (NO en GitHub)
├── .env.example              ← Template (EN GitHub)
├── .gitignore                ← Actualizado (.env incluido)
├── DEPLOY_ALWAYSDATA.md      ← Guía AlwaysData (NUEVO)
├── README.md                 ← Actualizado
├── dockerfile, docker-compose.yml, etc. ← Se mantienen
└── portfolio/
    └── settings.py           ← Actualizado para AlwaysData
```

## 🔄 Flujo de Configuración en AlwaysData

1. **Crear BD PostgreSQL** en AlwaysData panel
2. **Clonar repo**: `git clone ...`
3. **Instalar deps**: `pip install -r requirements.txt`
4. **Crear `.env`**: con credenciales BD
5. **Ejecutar migraciones**: `python manage.py migrate --noinput`
6. **Recopilar estáticos**: `python manage.py collectstatic --noinput`
7. **Configurar WSGI**: apuntar a `portfolio.wsgi:application`
8. **Reiniciar app**

## 🎯 Beneficios

✅ **Flexible**: Soporta múltiples hostings sin cambios de código
✅ **Seguro**: Credenciales en archivo local, no en GitHub
✅ **Compatible**: Mantiene Render, Docker, Heroku funcionando
✅ **Documentado**: Guía clara para cada plataforma
✅ **Production-ready**: Con DEBUG=False, SECRET_KEY segura, etc.

## 📝 Notas Importantes

- **El `.env` no se sincroniza**: Se crea directamente en AlwaysData
- **Cambiar BD es fácil**: Solo actualiza `.env`
- **Para desarrollo local**: Copia `.env.example` a `.env` con valores locales
- **Render aún funciona**: Si crear `DATABASE_URL` en Render, sigue trabajando

## ¿Preguntas?

- **¿Cómo cambiar de hosting?** → Actualiza `.env` con nuevas credenciales
- **¿Cómo volver a Render?** → Configura `DATABASE_URL` en Render
- **¿Archivos estáticos no cargan?** → Ejecuta `python manage.py collectstatic --noinput`
- **¿Media no carga?** → Verifica `MEDIA_ROOT` y permisos de carpeta
