from django.db import models


class Edificio(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return f"Edificio: {self.nombre}"


class Habitacion(models.Model):
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return f"Habitacion: {self.nombre} en edificio {self.edificio.nombre}"

    class Meta:
        verbose_name = "habitación"
        verbose_name_plural = "habitaciones"
