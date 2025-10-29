# 🔧 Solución para Archivos Media en Render

## Problema
Las imágenes y archivos PDF no se muestran en producción (Render).

## Causa
El `.dockerignore` estaba excluyendo la carpeta `media/`, impidiendo que los archivos se copiaran al contenedor de Docker.

## Solución Aplicada

### 1. ✅ Actualizado `.dockerignore`
- Eliminada la línea `media/` para que los archivos se incluyan en la imagen Docker

### 2. ✅ Actualizado `Dockerfile`
- Agregados permisos correctos a la carpeta `media/` (755)

### 3. ✅ Actualizado `portfolio/urls.py`
- Los archivos media ahora se sirven en producción (no solo en DEBUG=True)
- Agregado endpoint `/health/` que muestra archivos media disponibles

### 4. ✅ Archivos ya están en Git
```
media/about/IMG_1034.jpg
media/blog/1761566548977.jpg
media/cv/cvv.pdf
media/projects/rule.png
```

## 🚀 Siguientes Pasos

### 1. Hacer commit y push
```bash
git add .
git commit -m "Fix: Servir archivos media en producción (imágenes y PDFs)"
git push origin main
```

### 2. Verificar en Render
Espera 5-10 minutos a que Render reconstruya la imagen.

### 3. Probar
- Visita: `https://tu-portfolio.onrender.com/health/`
- Deberías ver: `"media_exists": true` y una lista de archivos
- Las imágenes deberían cargarse correctamente en:
  - Página "Sobre Mí" (foto de perfil)
  - Blog (imágenes de posts)
  - Proyectos (screenshots)
  - CV (botón descargar)

## 📝 Nota Importante

**Limitación del plan Free de Render:**
- Los archivos media se incluyen en la imagen Docker
- Si subes nuevos archivos desde el admin, se perderán al redesplegar
- Para archivos persistentes, necesitarías un servicio de almacenamiento externo (S3, Cloudinary, etc.)

**Para tu portfolio esto está bien porque:**
- Los archivos ya están en Git
- Solo cambias contenido ocasionalmente
- Al redesplegar, se restauran desde Git

## 🔍 Debug

Si después del deploy las imágenes NO se ven:

1. Ve a: `https://tu-portfolio.onrender.com/health/`
2. Verifica que `"media_exists": true`
3. Verifica que `"sample_files"` lista tus archivos
4. Si están vacíos, revisa los logs de build en Render
