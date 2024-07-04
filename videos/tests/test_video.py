from django.urls import reverse
import pytest
from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('videos:video', args=('motivacao',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_videos(resp):
    assert_contains(resp, '<h1 class="mt-4 mb-3">Video: Motivação</h1>')


def test_content_video(resp):
    assert_contains(
        resp, 'src="https://player.vimeo.com/video/973584504?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479"')
