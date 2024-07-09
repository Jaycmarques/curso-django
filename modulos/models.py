from django.db import models
from ordered_model.models import OrderedModel


class Modulo(OrderedModel):
    titulo = models.CharField(max_length=64)
    publico = models.TextField(default='Público padrão')
    descricao = models.TextField(default='Descrição padrão')

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self) -> str:
        return self.titulo
