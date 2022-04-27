from django.db import models


class Menu(models.Model):
    padre = models.ForeignKey('Menu', related_name="hijos", on_delete=models.SET_NULL, blank=True, null=True)
    nombre = models.CharField(max_length=20)

    def __str__(self):
        if self.padre:
            return f"{self.padre}/{self.nombre}"
        else:
            return f"{self.nombre}"
