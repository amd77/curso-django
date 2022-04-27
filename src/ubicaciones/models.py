from django.db import models


class Edificio(models.Model):
    nombre = models.CharField(max_length=20)
    habitacion_principal = models.ForeignKey('Habitacion', on_delete=models.SET_NULL, blank=True, null=True, related_name="adf")
    ususario = models.ForeignKey('auth.User', on_delete=models.SET_NULL, blank=True, null=True)

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
