from django.shortcuts import render
from django.shortcuts import HttpResponse


def pagina_inicial(request):
    return HttpResponse('Pronto para investir!')

def contato(request):
    return HttpResponse('Encaminhe um e-mail para leopoldo@ufjf.br')

def minha_historia(request):
    pessoa = {
        'nome':'Leopoldo',
        'idade': 28,
        'hobby': 'games'
    }
    return render(request,'investimentos/minha_historia.html',pessoa)