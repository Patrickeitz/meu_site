from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bem-vindo à Home</h1><p>Esta é a página inicial.</p>")

def contato(request):
    return HttpResponse("<h1>Página de Contato</h1><p>Email: exemplo@email.com</p>")
