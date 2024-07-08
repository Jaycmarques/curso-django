from typing import List
from modulos.models import Modulo


def listar_modulos_ordenados() -> List[Modulo]:
    '''
    Lista módulos ordenados por titulo
    :return:
    '''

    return list(Modulo.objects.order_by('titulo').all())