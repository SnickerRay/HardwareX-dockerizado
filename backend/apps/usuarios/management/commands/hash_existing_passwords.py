from django.contrib.auth.hashers import (
    identify_hasher,
    is_password_usable,
    make_password,
)
from django.core.management.base import BaseCommand
from django.db import transaction

from apps.usuarios.models import Usuario


class Command(BaseCommand):
    help = "Convierte las contraseñas antiguas a hashes seguros."

    @transaction.atomic
    def handle(self, *args, **options):
        convertidas = 0
        existentes = 0

        for usuario in Usuario.objects.all().iterator():
            clave = usuario.clave

            if not is_password_usable(clave):
                existentes += 1
                continue

            try:
                identify_hasher(clave)
                existentes += 1
                continue
            except ValueError:
                pass

            usuario.clave = make_password(clave)
            usuario.save(update_fields=["clave"])
            convertidas += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Conversión terminada. Convertidas: {convertidas}. "
                f"Ya protegidas o inutilizables: {existentes}."
            )
        )