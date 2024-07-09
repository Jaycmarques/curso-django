from django.shortcuts import render
from modulos import facade


def detalhe(request, slug):
    modulo = facade.encontrar_modulo(slug)
    return render(request, 'modulos/modulos_detalhe.html', {'modulo': modulo})
