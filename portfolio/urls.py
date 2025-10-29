"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse

def health_check(request):
    """Simple health check endpoint para Render"""
    return JsonResponse({'status': 'ok', 'service': 'portfolio'})

urlpatterns = [
    path('health/', health_check, name='health_check'),
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('projects/', include('apps.projects.urls')),
    path('about/', include('apps.about.urls')),
    path('contact/', include('apps.contact.urls')),
    path('services/', include('apps.services.urls')),
    path('testimonials/', include('apps.testimonials.urls')),
    path('techs/', include('apps.techs.urls')),
    path('blog/', include('apps.blog.urls')),
    path('resume/', include('apps.resume.urls')),
]

# Servir archivos media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Handler para errores
handler500 = 'portfolio.error_handlers.custom_500'
