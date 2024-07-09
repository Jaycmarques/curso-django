from django.urls import path
from modulos import views

app_name = 'modulos'
urlpatterns = [
    path('<slug:slug>', views.detalhe, name='detalhe'),
    # path("__debug__/", include("debug_toolbar.urls")),
]
