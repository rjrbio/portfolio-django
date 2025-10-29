"""
Vista para servir archivos media en producción
"""
import os
from django.conf import settings
from django.http import FileResponse, Http404
from django.views.decorators.cache import cache_control

@cache_control(max_age=3600)  # Cache por 1 hora
def serve_media(request, path):
    """Servir archivos media en producción"""
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    
    if not os.path.exists(file_path):
        raise Http404("Archivo no encontrado")
    
    return FileResponse(open(file_path, 'rb'))
