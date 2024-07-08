from django.urls import reverse
import pytest
from modulos.models import Modulo
from pypro.django_assertions import assert_contains
from model_bakery import baker


@pytest.fixture
def modulos(db):
    return baker.make(Modulo, 2)


@pytest.fixture
def resp(client, modulos):
    resp = client.get(reverse('base:home'))
    return resp


def test_titulos_modulos(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.titulo)
