from django.db import models

# Create your models here.

class Edificio(models.Model):
    """ """
    nombre = models.CharField("Nombre del edificio", max_length=100)
    direccion = models.CharField("Dirección", max_length=200)
    ciudad = models.CharField("Ciudad", max_length=100)
    tipo = models.CharField("Tipo de edificio", max_length=50) # residencial, comercial

    def __str__(self):
        return "Edificio: %s - Ciudad: %s - Tipo: %s" % (
            self.nombre,
            self.ciudad,
            self.tipo
        )


class Departamento(models.Model):
    """ """
    nombre_propietario = models.CharField("Nombre completo del propietario", max_length=150)
    costo_departamento = models.DecimalField("Costo del departamento", max_digits=12, decimal_places=2)
    num_cuartos = models.IntegerField("Número de cuartos")
    
    # Relación: Un departamento pertenece a un edificio
    edificio = models.ForeignKey(
        Edificio, related_name="mis_departamentos", on_delete=models.CASCADE
    )

    def __str__(self):
        return "Propietario: %s - Costo: $%s - Cuartos: %d" % (
            self.nombre_propietario,
            str(self.costo_departamento),
            self.num_cuartos
        )