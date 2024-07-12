from typing import List
from modulos.models import Modulo, Aula


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
