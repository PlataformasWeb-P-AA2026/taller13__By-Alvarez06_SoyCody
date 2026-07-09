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

