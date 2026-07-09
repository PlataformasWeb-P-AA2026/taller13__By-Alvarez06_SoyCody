from django.urls import path, include
# se importa las vistas de la aplicación
from inmobiliaria import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'edificios', views.EdificioViewSet)
router.register(r'departamentos', views.DepartamentoViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path("edificios/", views.listar_edificios, name="listar_edificios"),
    path("departamentos/", views.listar_departamentos, name="listar_departamentos"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]