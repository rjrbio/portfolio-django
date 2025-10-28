from django.shortcuts import render

def tech_list(request):
    """Lista de tecnologías"""
    return render(request, 'techs/list.html', {
        'techs': []
    })
