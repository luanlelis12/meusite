from django.urls import path
from .views import entrar, sair, cadastrar

urlpatterns = [
    path('entrar/', entrar),
    path('sair/', sair),
    path('cadastrar/', cadastrar),
]