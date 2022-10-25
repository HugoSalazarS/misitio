from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=100, label="Nombre", required=True,       widget=forms.TextInput(attrs={'placeholder': 'Escribe tu nombre', 'class': 'form-control'}))
    email = forms.EmailField(max_length=100, label="Email", required=True, widget=forms.EmailInput(attrs={'placeholder': 'Escribe tu correo', 'class': 'form-control'}))
    content = forms.CharField(max_length=500, label="Mensaje", required=True, widget=forms.Textarea(attrs={'placeholder': 'Escribe tu mensaje', 'rows': 3, 'class': 'form-control'}))