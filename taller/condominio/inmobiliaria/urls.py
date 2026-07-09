from django.urls import path, include
# se importa las vistas de la aplicación
from inmobiliaria import views

urlpatterns = [
    path('', views.index, name='index'),
    path("edificios/", views.listar_edificios, name="listar_edificios"),
    path("departamentos/", views.listar_departamentos, name="listar_departamentos"),
]