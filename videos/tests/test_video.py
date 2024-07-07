from django.urls import reverse
import pytest
from pypro.django_assertions import assert_contains
from videos.models import Video
from model_bakery import baker


@pytest.fixture
def video(db):
    return baker.make(Video)


@pytest.fixture
def resp(client, video):
    return client.get(reverse('videos:video', args=(video.slug,)))


@pytest.fixture
def resp_not_found_video(client, video):
    return client.get(reverse('videos:video', args=(video.slug + 'not_found_video',)))


def test_status_code_not_found(resp_not_found_video):
    assert resp_not_found_video.status_code == 404


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_videos(resp, video):
    assert_contains(resp, video.titulo)


def test_content_video(resp, video):
    assert_contains(
        resp, f'src="https://player.vimeo.com/video/{video.vimeo_id}?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479"')
