from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CadastroUsuarioForm(UserCreationForm):
    
    first_name = forms.CharField(label = 'Primeiro Nome', max_length=50, required=True, help_text='Campo obrigatório')
    last_name = forms.CharField(label = 'Último Nome', required=False, help_text='Campo obrigatório')
    email = forms.EmailField(label = 'E-mail', max_length=250, help_text='Por favor insira o email corretamente')

    class Meta:
        models = User
        fields = ['username', 'primeiro_nome', 'ultimo_nome', 'email', 'password1', 'password2']