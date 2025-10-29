"""
Vista personalizada para errores 500 en producción
"""
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def custom_500(request):
    """Handler personalizado para errores 500"""
    logger.error("Error 500 detectado", exc_info=True)
    
    if request.path.startswith('/api/'):
        return JsonResponse({
            'error': 'Internal Server Error',
            'message': 'Ha ocurrido un error en el servidor'
        }, status=500)
    
    from django.shortcuts import render
    return render(request, '500.html', status=500)
