from django.urls import path
from base.views import home

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
    # path("__debug__/", include("debug_toolbar.urls")),
]
