from django.shortcuts import render, HttpResponse
from .forms import ContactForm 

# Create your views here.
html_base = """
    <h1> Hugo Salazar</h1>
    <ul>
        <li><a href='/'>Portada</a></li>
        <li><a href='/about'>Sobre mi</a></li>
        <li><a href='/portfolio'>Mi portfolio</a></li>
        <li><a href='/contact'>Contacto</a></li>
    </ul>
    """

def home(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def portfolio(request):
    return render(request, 'core/portfolio.html')


def contact(request):
    contact_form = ContactForm
    
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = request.POST.get['name']
            email = request.POST.get['email']
            content = request.POST.get['content']
    else:
        contact_form = ContactForm()
        return render(request, 'core/contact.html', {'form': contact_form})





