from django.urls import reverse
import pytest
from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('videos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'titulo', [
        'Video: Motivação',
        'Instalação Windows',
    ]
)
def test_title_videos(resp, titulo):
    assert_contains(resp, titulo)


# def test_content_video(resp):
#     assert_contains(
#         resp, 'src="https://player.vimeo.com/video/973584504?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479"')
