from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.projects.models import Project
from apps.projects.serializers import ProjectSerializer
from apps.services.models import Service
from apps.services.serializers import ServiceSerializer
from apps.testimonials.models import Testimonial
from apps.testimonials.serializers import TestimonialSerializer
from apps.blog.models import Post
from apps.blog.serializers import PostListSerializer


@api_view(['GET'])
def home(request):
    ctx = {'request': request}
    featured_qs = Project.objects.filter(featured=True).order_by('-created_at')
    if not featured_qs.exists():
        # Fallback para evitar home vacía si no hay proyectos marcados como destacados.
        featured_qs = Project.objects.all().order_by('-created_at')

    data = {
        'featured_projects': ProjectSerializer(
            featured_qs[:3],
            many=True, context=ctx
        ).data,
        'services': ServiceSerializer(
            Service.objects.all()[:4], many=True, context=ctx
        ).data,
        'testimonials': TestimonialSerializer(
            Testimonial.objects.all()[:3], many=True, context=ctx
        ).data,
        'recent_posts': PostListSerializer(
            Post.objects.filter(published=True).order_by('-created_at')[:3],
            many=True, context=ctx
        ).data,
    }
    return Response(data)
