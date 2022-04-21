from django.contrib import admin
from .models import Edificio, Habitacion


@admin.register(Edificio)
class EdificioAdmin(admin.ModelAdmin):
    pass


@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    pass
