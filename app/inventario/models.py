from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    fechaIngreso = models.DateField(auto_now_add=True)
    comentario = models.TextField()
