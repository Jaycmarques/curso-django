from django.urls import reverse
import pytest
from modulos.models import Aula, Modulo
from pypro.django_assertions import assert_contains
from model_bakery import baker


@pytest.fixture
def modulo(db):
    return baker.make(Modulo)


@pytest.fixture
def aula(modulo):
    return baker.make(Aula, modulo=modulo)


@pytest.fixture
def resp(client, aula):
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


def test_titulo(resp, aula: Aula):
    assert_contains(resp, aula.titulo)


def test_vimeo(resp, aula: Aula):
    assert_contains(
        resp, f'src="https://player.vimeo.com/video/{aula.vimeo_id}?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479"')


def test_modulo_breadcrumb(resp, modulo: Modulo):
    assert_contains(resp, f'<li class="breadcrumb-item"><a href="{modulo.get_absolute_url()}">{modulo.titulo}</a></li>'
                    )