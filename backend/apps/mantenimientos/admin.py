from django.contrib import admin

from .models import Mantenimiento


@admin.register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):

    list_display = (
        "id_mantenimiento",
    )