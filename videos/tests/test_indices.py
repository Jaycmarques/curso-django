from django.urls import reverse
import pytest
from pypro.django_assertions import assert_contains
from model_bakery import baker

from videos.models import Video


@pytest.fixture
def videos(db):
    return baker.make(Video, 3)


@pytest.fixture
def resp(client, videos):
    return client.get(reverse('videos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_videos(resp, videos):
    for video in videos:
        assert_contains(resp, video.titulo)


def test_link_videos(resp, videos):
    for video in videos:
        video_link = reverse('videos:video', args=(video.slug,))
        assert_contains(resp, f'href="{video_link}"')
