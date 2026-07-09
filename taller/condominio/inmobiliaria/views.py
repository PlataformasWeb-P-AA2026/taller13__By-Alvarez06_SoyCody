from django.shortcuts import render
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

