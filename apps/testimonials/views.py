from django.shortcuts import render

def testimonial_list(request):
    """Lista de testimonios"""
    return render(request, 'testimonials/list.html', {
        'testimonials': []
    })
