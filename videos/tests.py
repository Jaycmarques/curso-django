
from django.urls import reverse
import pytest
from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('videos:video', args=('motivacao',)))


def teste_status_code(resp):
    assert resp.status_code == 200


def test_title_video(resp):
    assert_contains(resp, '<h1>Video: Motivação</h1>')


def test_conteudo_video(resp):
    assert_contains(resp, '<iframe src="https://player.vimeo.com/video/973584504?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Hotmart Club - 12- Como criar e exportar um Carrossel para Instagram usando Artboards - Google Chrome 2021-05-01 19-02-13"></iframe>')

    # <div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/973584504?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Hotmart Club - 12- Como criar e exportar um Carrossel para Instagram usando Artboards - Google Chrome 2021-05-01 19-02-13"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>
