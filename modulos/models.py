from django.db import models
from django.urls import reverse
from ordered_model.models import OrderedModel


class Modulo(OrderedModel):
    titulo = models.CharField(max_length=64)
    publico = models.TextField(default='Público padrão')
    descricao = models.TextField(default='Descrição padrão')
    slug = models.SlugField(unique=True, max_length=32)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self) -> str:
        return self.titulo

    def get_absolute_url(self):
        return reverse('modulos:detalhe', kwargs={'slug': self.slug})


class Aula(OrderedModel):
    titulo = models.CharField(max_length=64)
    slug = models.SlugField(unique=True, max_length=32)
    modulo = models.ForeignKey('Modulo', on_delete=models.PROTECT)
    order_with_respect_to = 'modulo'
    vimeo_id = models.CharField(max_length=32)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self) -> str:
        return self.titulo

    def get_absolute_url(self):
        return reverse('modulos:aula', kwargs={'slug': self.slug})
