from django.db import models

# Create your models here.

class Edificio(models.Model):
    opciones_tipo_Edificio = (
        ('Residencial', 'Residencial'),
        ('Comercial', 'Comercial'),
         ('Negocio','Negocio'),
         ('Público', 'Público')
    )
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30,\
                            choices= opciones_tipo_Edificio)



class Propietario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.IntegerField()
    def __str__(self):
        return "%s %s %s" % (self.nombre,
                self.apellido,
                self.cedula)


 
          
class Departamento(models.Model):
    costo = models.IntegerField()
    numero_cuartos = models.IntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="numero_departamentos")
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE,
            related_name="departamentos")
    def __str__(self):
        return "%d %d %s %s" % (self.costo,
                self.numero_cuartos,
                self.edificio,
                self.propietario)