from distutils import core
from django.shortcuts import render, redirect
from core.forms import ContactForm
from django.urls import reverse

from django.core.mail import send_mail
from misitio.settings import EMAIL_HOST_USER 
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
    contact_form = ContactForm
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
    
        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('content')
            send_mail(request)
            return redirect(reverse('contact') + '?ok')
        
    return render(request, 'contact/contact.html', {'form': contact_form})

def send_mail(request):
    name = request.POST.get('name')
    mail = request.POST.get('email')
    content = request.POST.get('content')
    
    email = EmailMessage(
        "Nuevo mensaje de contacto de portfolio en django",
        "De {} <{}>\n\nEscribió:\n\n{}".format(name, mail, content),
        EMAIL_HOST_USER,
        ['20cbd061cafb'],
        reply_to=['email']
        
    )
    try:
        email.send()

        return redirect(reverse('contact') + '?ok')

    except:

        return redirect(reverse('contact') + '?fail')
    
    


