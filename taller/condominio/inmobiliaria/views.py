from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer, EdificioSerializer, DepartamentoSerializer
from .models import Edificio, Departamento

# Create your views here.
def index(request):
    """
    Listar los registros de los modelos Edificio y Departamento,
    obtenidos de la base de datos para su presentación en tablas.
    """
    edificios = Edificio.objects.all()
    departamentos = Departamento.objects.all()
    
    informacion_template = {
        "edificios": edificios,
        "numero_edificios": len(edificios),
        "departamentos": departamentos,
        "numero_departamentos": len(departamentos),
    }
    
    return render(request, "index.html", informacion_template)

def listar_edificios(request):
    """
    Listar únicamente los registros del modelo Edificio.
    """
    edificios = Edificio.objects.all()
    
    informacion_template = {
        "edificios": edificios,
        "numero_edificios": len(edificios),
    }
    
    return render(request, "listar_edificios.html", informacion_template)


def listar_departamentos(request):
    """
    Listar únicamente los registros del modelo Departamento.
    """
    departamentos = Departamento.objects.all()
    
    informacion_template = {
        "departamentos": departamentos,
        "numero_departamentos": len(departamentos),
    }
    
    return render(request, "listar_departamentos.html", informacion_template)

# crear vistas a través de viewsets
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class EdificioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows edificios to be viewed or edited.
    """
    queryset = Edificio.objects.all()
    serializer_class = EdificioSerializer
    permission_classes = [permissions.IsAuthenticated]

class DepartamentoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows departamentos to be viewed or edited.
    """
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [permissions.IsAuthenticated]