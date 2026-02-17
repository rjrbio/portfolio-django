# Deploy en AlwaysData

Guía paso a paso para migrar el portfolio de Render a AlwaysData.

## 1. Crear la Base de Datos PostgreSQL

1. Entra al panel de AlwaysData
2. Ve a **PostgreSQL** → **Add a database**
3. Guarda los datos que te proporciona:
   - Host PostgreSQL
   - Usuario
   - Contraseña
   - Nombre de la base de datos
   - Puerto (normalmente 5432)

## 2. Crear la Aplicación Python WSGI

1. Ve a **Web** → **Add a site**
2. Selecciona:
   - **Name**: nombre de tu sitio (ej: `jdev`)
   - **Type**: Python WSGI
   - **Path**: `/home/jdev/www` (o la que uses)
   - **Commands**: instala Python 3.12

## 3. Clonar el Proyecto

En la consola de AlwaysData:

```bash
cd /home/jdev/www
git clone https://github.com/rjrbio/portfolio-django.git
cd portfolio-django
```

## 4. Instalar Dependencias

En la consola:

```bash
pip install -r requirements.txt
```

## 5. Crear el archivo `.env`

El archivo `.env` no viene en el repositorio (está en `.gitignore` por seguridad).

En la consola, crea el archivo:

```bash
cat > /home/jdev/www/portfolio-django/.env << 'EOF'
DEBUG=False
SECRET_KEY=tu-clave-secreta-fuerte-aqui
ALLOWED_HOSTS=tu-dominio.alwaysdata.net
CSRF_TRUSTED_ORIGINS=https://tu-dominio.alwaysdata.net
DB_NAME=nombre_de_bd
DB_USER=usuario_bd
DB_PASSWORD=contraseña_bd
DB_HOST=host-postgresql.alwaysdata.net
DB_PORT=5432
DB_SSLMODE=prefer
EOF
```

**Reemplaza los valores con los datos reales de tu BD.**

## 6. Ejecutar Migraciones

En la consola:

```bash
python manage.py migrate --noinput
```

## 7. Recopilar Archivos Estáticos

En la consola:

```bash
python manage.py collectstatic --noinput
```

## 8. (Opcional) Crear Superusuario

Si necesitas acceder al admin:

```bash
python manage.py createsuperuser
```

## 9. Configurar el WSGI en AlwaysData

En el panel:

1. Ve a **Web** → tu sitio → **Configuration**
2. **Application entry point**: `portfolio.wsgi:application`
3. **Reload on file change**: activa si quieres (desarrollo)
4. **Workers**: 2-4 (según tu plan)

## 10. Configurar Variables de Entorno (Opcional)

Si prefieres usar "Environment variables" en AlwaysData en lugar de `.env`:

En **Web configuration** → **Environment variables**:

```
DEBUG=False
SECRET_KEY=tu-clave-secreta
ALLOWED_HOSTS=tu-dominio.alwaysdata.net
CSRF_TRUSTED_ORIGINS=https://tu-dominio.alwaysdata.net
DB_NAME=nombre_db
DB_USER=usuario_db
DB_PASSWORD=contraseña_db
DB_HOST=host_postgresql.alwaysdata.net
DB_PORT=5432
DB_SSLMODE=prefer
```

## 11. Reiniciar la Aplicación

En el panel de AlwaysData, haz clic en **Restart** o **Reload**.

## Troubleshooting

### Error: "could not translate host name"
- Verifica que el host de PostgreSQL en `.env` es correcto
- Asegúrate de tener conexión a la BD

### Error: "Couldn't import Django"
- Ejecuta: `pip install -r requirements.txt`
- Verifica que Python 3.12 está seleccionado

### Media no se muestra
- Verifica que `MEDIA_ROOT = BASE_DIR / "media"` en settings.py
- La carpeta `media/` debe ser writable por el usuario de AlwaysData

### Cambios no se reflejan
- Haz **Restart** en AlwaysData
- Borra la cache del navegador (Ctrl+Shift+Delete)

## Notas

- El archivo `.env` **no se sube a GitHub** (está en `.gitignore`)
- Las credenciales de base de datos están protegidas en el `.env` local
- Usa `DEBUG=False` siempre en producción
- `SECRET_KEY` debe ser larga y aleatoria
