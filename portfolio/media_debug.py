from django.http import JsonResponse
from django.conf import settings
import os

def media_debug(request):
    """Debug detallado de archivos media"""
    from apps.about.models import About
    from apps.blog.models import Post
    from apps.projects.models import Project
    
    debug_info = {
        'settings': {
            'MEDIA_URL': settings.MEDIA_URL,
            'MEDIA_ROOT': str(settings.MEDIA_ROOT),
            'DEBUG': settings.DEBUG,
        },
        'media_directory': {
            'exists': os.path.exists(settings.MEDIA_ROOT),
            'contents': []
        },
        'database_records': {}
    }
    
    # Listar archivos en media
    if os.path.exists(settings.MEDIA_ROOT):
        for root, dirs, files in os.walk(settings.MEDIA_ROOT):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, settings.MEDIA_ROOT)
                debug_info['media_directory']['contents'].append({
                    'path': rel_path,
                    'size': os.path.getsize(full_path),
                    'exists': os.path.exists(full_path)
                })
    
    # Verificar registros en BD
    try:
        about = About.objects.first()
        if about:
            debug_info['database_records']['about'] = {
                'profile_image_field': str(about.profile_image) if about.profile_image else None,
                'profile_image_url': about.profile_image.url if about.profile_image else None,
                'cv_file_field': str(about.cv_file) if about.cv_file else None,
                'cv_file_url': about.cv_file.url if about.cv_file else None,
            }
    except Exception as e:
        debug_info['database_records']['about_error'] = str(e)
    
    try:
        post = Post.objects.filter(image__isnull=False).first()
        if post:
            debug_info['database_records']['blog_post'] = {
                'image_field': str(post.image),
                'image_url': post.image.url,
                'image_path_exists': os.path.exists(post.image.path) if post.image else False
            }
    except Exception as e:
        debug_info['database_records']['blog_error'] = str(e)
    
    try:
        project = Project.objects.filter(image__isnull=False).first()
        if project:
            debug_info['database_records']['project'] = {
                'image_field': str(project.image),
                'image_url': project.image.url,
                'image_path_exists': os.path.exists(project.image.path) if project.image else False
            }
    except Exception as e:
        debug_info['database_records']['project_error'] = str(e)
    
    return JsonResponse(debug_info, json_dumps_params={'indent': 2})
