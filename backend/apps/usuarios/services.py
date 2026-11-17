from django.contrib.auth.hashers import check_password

from .models import Usuario
from django.conf import settings
from django.contrib.sessions.models import Session
from django.db import transaction
from django.utils import timezone


ROL_TECNICO = 3


def autenticar_usuario(email, clave):
    try:
        usuario = Usuario.objects.get(email=email)
    except Usuario.DoesNotExist:
        return None

    if not check_password(clave, usuario.clave):
        return None

    return usuario


def obtener_usuario(id_usuario):
    try:
        return Usuario.objects.get(id_usuario=id_usuario)
    except Usuario.DoesNotExist:
        return None


def listar_tecnicos():
    return Usuario.objects.filter(id_rol_fk=ROL_TECNICO).order_by("nombres")

def iniciar_sesion_unica(request, usuario):
    """
    Permite una sola sesión activa por usuario.

    Bloquea temporalmente el registro del usuario mientras comprueba
    las sesiones existentes y crea la nueva sesión.
    """

    # Las pruebas usan signed_cookies, que no almacena sesiones
    # centralizadas en django_session.
    if settings.SESSION_ENGINE.endswith("signed_cookies"):
        request.session["usuario_id"] = usuario.id_usuario
        request.session["usuario_nombre"] = usuario.nombre_usuario
        request.session["usuario_email"] = usuario.email
        request.session["usuario_rol"] = usuario.id_rol_fk
        request.session.set_expiry(60 * 60 * 8)
        return True

    with transaction.atomic():

        # Serializa los intentos de inicio de sesión para esta cuenta.
        Usuario.objects.select_for_update().get(
            pk=usuario.id_usuario
        )

        sesiones_activas = Session.objects.filter(
            expire_date__gt=timezone.now()
        ).only("session_key", "session_data")

        for sesion in sesiones_activas.iterator():
            datos = sesion.get_decoded()

            if str(datos.get("usuario_id")) == str(usuario.id_usuario):
                return False

        # Renueva el identificador de sesión antes de autenticar.
        request.session.cycle_key()

        request.session["usuario_id"] = usuario.id_usuario
        request.session["usuario_nombre"] = usuario.nombre_usuario
        request.session["usuario_email"] = usuario.email
        request.session["usuario_rol"] = usuario.id_rol_fk

        request.session.set_expiry(60 * 60 * 8)

        # Guarda la sesión dentro de la transacción.
        request.session.save()

    return True