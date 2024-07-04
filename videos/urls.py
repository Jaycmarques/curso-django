from django.urls import path
from videos.views import video, indice

app_name = 'videos'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
    path('', indice, name='indice'),

    # path("__debug__/", include("debug_toolbar.urls")),
]
