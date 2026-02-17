# ✅ Checklist de Migración a AlwaysData

Usa este checklist para verificar que todo está configurado correctamente.

## 📋 Pre-Deploy en AlwaysData

- [ ] BD PostgreSQL creada en AlwaysData
- [ ] Datos de BD anotados (host, usuario, contraseña, nombre, puerto)
- [ ] App Python WSGI creada en AlwaysData
- [ ] Python 3.12 seleccionado
- [ ] Proyecto clonado: `git clone https://github.com/rjrbio/portfolio-django.git`

## 🔧 Instalación en Servidor

- [ ] Dependencias instaladas: `pip install -r requirements.txt`
- [ ] Archivo `.env` creado en `/home/usuario/www/portfolio-django/.env`
- [ ] `.env` contiene credenciales correctas:
  - [ ] `DEBUG=False`
  - [ ] `SECRET_KEY=valor-largo-aleatorio`
  - [ ] `DB_NAME=nombre_correcto` (ejemplo: `jdev_db`)
  - [ ] `DB_USER=usuario_correcto` (ejemplo: `jdev`)
  - [ ] `DB_PASSWORD=contraseña_correcta`
  - [ ] `DB_HOST=postgresql-jdev.alwaysdata.net`
  - [ ] `DB_PORT=5432`
  - [ ] `ALLOWED_HOSTS=tu-dominio.alwaysdata.net`
  - [ ] `CSRF_TRUSTED_ORIGINS=https://tu-dominio.alwaysdata.net`

## 🗄️ Configuración de Base de Datos

- [ ] Conexión a BD probada: `python manage.py dbshell` (debe abrir consola)
- [ ] Migraciones ejecutadas: `python manage.py migrate --noinput`
- [ ] NO hay errores de migración
- [ ] Archivos estáticos copiados: `python manage.py collectstatic --noinput`

## 🎯 Configuración Web

- [ ] WSGI configurado en AlwaysData: `portfolio.wsgi:application`
- [ ] Workers: 2-4 según plan
- [ ] Reload on change: desactivado en producción
- [ ] App reiniciada en AlwaysData

## 🧪 Pruebas

- [ ] Accedible en `https://tu-dominio.alwaysdata.net`
- [ ] Homepage carga correctamente
- [ ] Admin accessible en `/admin`
- [ ] Admin login funciona (superusuario creado)
- [ ] Imágenes cargan correctamente
- [ ] CSS/JS cargan sin errores
- [ ] Sin errores 500

## 📱 Funcionalidad

- [ ] Secciones principales cargan:
  - [ ] Home
  - [ ] Projects
  - [ ] Blog
  - [ ] About
  - [ ] Resume
  - [ ] Contact
  - [ ] Services
  - [ ] Testimonials
- [ ] Formulario de contacto funciona
- [ ] Admin panel funciona
- [ ] Crear/editar contenido en admin funciona

## 📊 Monitoreo

- [ ] Error logs monitoreados
- [ ] BD permisos correctos (app puede escribir/leer)
- [ ] Carpeta `media/` es writable
- [ ] Carpeta `staticfiles/` es writable
- [ ] Plan de backup de BD establecido

## 🛡️ Seguridad

- [ ] `DEBUG=False` en producción
- [ ] `SECRET_KEY` es larga y aleatoria (50+ caracteres)
- [ ] `.env` NO está en GitHub
- [ ] `.env` NO es accesible públicamente
- [ ] HTTPS habilitado
- [ ] CSRF_TRUSTED_ORIGINS configurado correctamente
- [ ] ALLOWED_HOSTS restringido a tus dominios

## 📝 Documentación

- [ ] `DEPLOY_ALWAYSDATA.md` actualizado con tu info
- [ ] `.env.example` actualizado (si cambiaron variables)
- [ ] `README.md` actualizado (si hay cambios específicos)
- [ ] Tu equipo tiene acceso a esta guía

## 🎉 Post-Deploy

- [ ] ¿Todo funciona? Celebra 🎊
- [ ] ¿Hay problema? Revisa sección **Troubleshooting** en `DEPLOY_ALWAYSDATA.md`
- [ ] Configura monitoreo (error tracking, performance)
- [ ] Backup automático de BD configurado

---

## 🆘 Troubleshooting Rápido

| Error | Solución |
|-------|----------|
| `.env` no encontrado | Verifica que está en `/home/usuario/www/portfolio-django/.env` |
| BD no conecta | Verifica credenciales en `.env`, host accesible |
| Estáticos no cargan | Ejecuta `collectstatic`, reinicia app |
| 500 error | Revisa logs, comprueba `DEBUG=False` permite logs |
| Admin no funciona | Crea superusuario: `python manage.py createsuperuser` |
| Media no muestra | Verifica `MEDIA_ROOT` permiso write, carpeta existe |

---

**¿Necesitas ayuda?** Consulta `DEPLOY_ALWAYSDATA.md` o `MIGRACION_RESUMEN.md`.
