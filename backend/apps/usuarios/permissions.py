from rest_framework.permissions import BasePermission

<<<<<<< HEAD

class EsUsuarioAutenticado(BasePermission):
    """
    Permiso base para usuarios autenticados.
    """

    message = "Debes estar autenticado para realizar esta acción."

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
=======
from .roles import (
    ROL_ADMINISTRADOR,
    ROL_USUARIO,
    ROL_TECNICO,
)


class EsUsuarioAutenticado(BasePermission):
    """
    Permite el acceso únicamente a usuarios con una sesión válida
    y un rol reconocido dentro de HardwareX.
    """

    message = "Debes iniciar sesión para realizar esta acción."

    def has_permission(self, request, view):
        usuario_id = request.session.get("usuario_id")
        rol = request.session.get("usuario_rol")

        return bool(
            usuario_id
            and rol in (
                ROL_ADMINISTRADOR,
                ROL_USUARIO,
                ROL_TECNICO,
            )
        )


class EsAdministrador(EsUsuarioAutenticado):
    """
    Permite el acceso únicamente al administrador.
    """

    message = "No tienes permisos para realizar esta acción."

    def has_permission(self, request, view):
        return (
            super().has_permission(request, view)
            and request.session.get("usuario_rol") == ROL_ADMINISTRADOR
        )


class EsTecnico(EsUsuarioAutenticado):
    """
    Permite el acceso al administrador y al técnico.
    """

    message = "No tienes permisos para realizar esta acción."

    def has_permission(self, request, view):
        return (
            super().has_permission(request, view)
            and request.session.get("usuario_rol") in (
                ROL_ADMINISTRADOR,
                ROL_TECNICO,
            )
        )


class EsUsuarioPropietario(EsUsuarioAutenticado):
    """
    Permite comprobar que el usuario autenticado
    solo pueda acceder a sus propios recursos.
    """

    message = "No tienes permisos para consultar esta información."

    def has_permission(self, request, view):
        return super().has_permission(request, view)

    def tiene_propiedad(self, request, id_usuario):
        rol = request.session.get("usuario_rol")
        usuario_id = request.session.get("usuario_id")

        return (
            rol == ROL_ADMINISTRADOR
            or str(usuario_id) == str(id_usuario)
        )
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
