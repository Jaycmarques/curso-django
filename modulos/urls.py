from django.urls import path
from modulos import views

app_name = 'modulos'
urlpatterns = [
    path('', views.indice, name='indice'),
    path('<slug:slug>', views.detalhe, name='detalhe'),
    path('aulas/<slug:slug>', views.aula, name='aula'),
    # path("__debug__/", include("debug_toolbar.urls")),
]
