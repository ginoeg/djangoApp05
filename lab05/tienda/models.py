from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre

class Producto(models.Model):
        Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
        nombre = models.CharField(max_length=200)
        precio = models.DecimalField(max_digits=6, decimal_places=2)
        stock = models.IntegerField(default=0)
        pub_date = models.DateTimeField('date published')

        def __str__(self):
            return self.nombre

class Cliente(models.Model):
        Nombre = models.CharField(max_length=200)
        apellidos = models.CharField(max_length=200)
        dni = models.CharField(max_length=9)
        telefono = models.CharField(max_length=10)
        direccion = models.CharField(max_length=100)
        email = models.EmailField()
        Fecha_nacimiento = models.DateField('fecha de nacimiento')
        fecha_publicacion = models.DateField('fecha de publicacion')

        def __str__(self):
            return self.Nombre

