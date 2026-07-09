from django.contrib.auth.models import User, Group
from .models import Edificio, Departamento
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class EdificioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Edificio
        # fields = ['id', 'nombre', 'direccion', 'ciudad', 'tipo']
        fields = '__all__'

class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        # fields = ['id', 'nombre_propietario', 'costo_departamento', 'num_cuartos',
        #           'edificio']
        fields = '__all__'