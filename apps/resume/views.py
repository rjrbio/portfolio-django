from django.shortcuts import render
from .models import Education, Experience
from apps.about.models import About

def resume(request):
    """Página de currículum"""
    education = Education.objects.all()
    experience = Experience.objects.all()
    about = About.objects.first()
    return render(request, 'resume/resume.html', {
        'education': education,
        'experience': experience,
        'about': about
    })
