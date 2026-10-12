from django.contrib import admin

from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):

    list_display = (
        "id_usuario",
        "nombre_usuario",
        "nombres",
        "apellidos",
        "email",
        "id_rol_fk",
    )

    search_fields = (
        "nombre_usuario",
        "email",
        "nombres",
        "apellidos",
    )