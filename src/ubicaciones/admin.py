from django.contrib import admin
from .models import Edificio, Habitacion

class HabitacionInline(admin.TabularInline):
    model = Habitacion


@admin.register(Edificio)
class EdificioAdmin(admin.ModelAdmin):
    inlines = [HabitacionInline]


@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    pass
