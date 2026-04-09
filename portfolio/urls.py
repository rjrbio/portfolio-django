from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView
from portfolio.media_debug import media_debug
from portfolio.media_serve import serve_media
import os


def health_check(request):
    media_files = []
    media_root = settings.MEDIA_ROOT
    if os.path.exists(media_root):
        for root, dirs, files in os.walk(media_root):
            for file in files[:5]:
                rel_path = os.path.relpath(os.path.join(root, file), media_root)
                media_files.append(rel_path)
    return JsonResponse({
        'status': 'ok',
        'service': 'portfolio',
        'media_root': str(media_root),
        'media_exists': os.path.exists(media_root),
        'sample_files': media_files,
    })


urlpatterns = [
    path('health/', health_check, name='health_check'),
    path('media-debug/', media_debug, name='media_debug'),
    path('admin/', admin.site.urls),

    # API v1
    path('api/v1/', include('apps.core.urls')),
    path('api/v1/projects/', include('apps.projects.urls')),
    path('api/v1/about/', include('apps.about.urls')),
    path('api/v1/contact/', include('apps.contact.urls')),
    path('api/v1/services/', include('apps.services.urls')),
    path('api/v1/testimonials/', include('apps.testimonials.urls')),
    path('api/v1/techs/', include('apps.techs.urls')),
    path('api/v1/blog/', include('apps.blog.urls')),
    path('api/v1/resume/', include('apps.resume.urls')),
    path('api/v1/agent/', include('apps.agent.urls')),

    # Media
    re_path(r'^media/(?P<path>.*)$', serve_media, name='media'),

    # Catch-all: devuelve el shell de Vue para cualquier ruta no-API
    re_path(r'^(?!api/|admin/|media/|health/|media-debug/).*$',
            TemplateView.as_view(template_name='spa.html'), name='spa'),
]

handler500 = 'portfolio.error_handlers.custom_500'
