from django.shortcuts import render
from apps.projects.models import Project
from apps.services.models import Service
from apps.testimonials.models import Testimonial
from apps.blog.models import Post

def home(request):
    context = {
        'featured_projects': Project.objects.filter(featured=True)[:3],
        'services': Service.objects.all()[:4],
        'testimonials': Testimonial.objects.all()[:3],
        'recent_posts': Post.objects.filter(published=True)[:3],
    }
    return render(request, 'core/home.html', context)
