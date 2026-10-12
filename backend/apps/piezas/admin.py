from django.contrib import admin

from .models import Pieza, TipoPieza


@admin.register(Pieza)
class PiezaAdmin(admin.ModelAdmin):
    list_display = (
        "id_pieza",
        "nombre",
        "id_tipo_pieza_fk",
    )


@admin.register(TipoPieza)
class TipoPiezaAdmin(admin.ModelAdmin):
    list_display = (
        "id_tipo_pieza",
        "nombre",
    )