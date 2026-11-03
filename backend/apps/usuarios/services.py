
from django.contrib.auth.hashers import (
    check_password,
    identify_hasher,
    make_password,
)
from django.utils.crypto import constant_time_compare

from .models import Usuario

ROL_TECNICO = 3  # TODO: confirmar el id real del rol "técnico" en tu base de datos


def autenticar_usuario(email, clave):
    try:
        usuario = Usuario.objects.get(email=email)
    except Usuario.DoesNotExist:
        return None

    try:
        identify_hasher(usuario.clave)
        es_hash = True
    except ValueError:
        es_hash = False

    if es_hash:
        if not check_password(clave, usuario.clave):
            return None
    else:
        if not constant_time_compare(clave, usuario.clave):
            return None

        usuario.clave = make_password(clave)
        usuario.save(update_fields=["clave"])

    return usuario


def obtener_usuario(id_usuario):
    try:
        return Usuario.objects.get(id_usuario=id_usuario)
    except Usuario.DoesNotExist:
        return None


def listar_tecnicos():
    return Usuario.objects.filter(id_rol_fk=ROL_TECNICO).order_by("nombres")
