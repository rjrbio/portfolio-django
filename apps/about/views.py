from django.shortcuts import render
from .models import About
from apps.techs.models import Technology

def about(request):
    """Página sobre mí"""
    about_info = About.objects.first()
    technologies = Technology.objects.all()
    return render(request, 'about/about.html', {
        'about': about_info,
        'technologies': technologies
    })
