from typing import List
from modulos.models import Modulo, Aula
from django.db.models import Prefetch


def listar_modulos_ordenados() -> List[Modulo]:
    '''
    Lista módulos ordenados por titulo
    :return:
    '''

    return list(Modulo.objects.order_by('titulo').all())


def encontrar_modulo(slug: str):
    return Modulo.objects.get(slug=slug)


def listar_aulas(modulo: Modulo):
    return list(modulo.aula_set.order_by('order').all())


def encontrar_aula(slug: str):
    return Aula.objects.select_related('modulo').get(slug=slug)


def listar_modulos_com_aulas() -> List[Modulo]:
    aulas_ordenadas = Aula.objects.order_by('order')
    return Modulo.objects.order_by('order').prefetch_related(Prefetch('aula_set', queryset=aulas_ordenadas, to_attr='aulas')).all()
