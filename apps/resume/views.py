from django.shortcuts import render
from .models import Education, Experience

def resume(request):
    """Página de currículum"""
    education = Education.objects.all()
    experience = Experience.objects.all()
    return render(request, 'resume/resume.html', {
        'education': education,
        'experience': experience
    })
