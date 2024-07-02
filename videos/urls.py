from django.urls import path
from videos.views import video

app_name = 'videos'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
    # path("__debug__/", include("debug_toolbar.urls")),
]
