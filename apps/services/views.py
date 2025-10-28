from django.shortcuts import render
from .models import Service

def service_list(request):
    """Lista de servicios"""
    services = Service.objects.all()
    return render(request, 'services/list.html', {
        'services': services
    })
