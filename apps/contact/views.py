from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def contact(request):
    """Página de contacto"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_text = request.POST.get('message')
        
        if name and email and subject and message_text:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_text
            )
            messages.success(request, '¡Mensaje enviado correctamente! Te responderé pronto.')
            return redirect('contact:contact')
        else:
            messages.error(request, 'Por favor, completa todos los campos.')
    
    return render(request, 'contact/contact.html', {})
