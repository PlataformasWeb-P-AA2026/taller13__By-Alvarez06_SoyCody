from django.urls import path, include
# se importa las vistas de la aplicación
from inmobiliaria import views

urlpatterns = [
    path('', views.index, name='index'),
]