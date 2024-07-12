from django.shortcuts import render
from modulos import facade


def detalhe(request, slug):
    modulo = facade.encontrar_modulo(slug)
    aulas = facade.listar_aulas(modulo)
    return render(request, 'modulos/modulos_detalhe.html', {'modulo': modulo, 'aulas': aulas})
