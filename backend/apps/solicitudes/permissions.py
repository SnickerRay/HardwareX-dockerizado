<<<<<<< HEAD
from rest_framework.permissions import BasePermission


class SolicitudPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated
=======

from apps.usuarios.permissions import (
    EsUsuarioAutenticado,
    EsAdministrador,
    EsTecnico,
    EsUsuarioPropietario,
)


class SolicitudPermission(EsUsuarioAutenticado):
    """
    Permite acceder a las solicitudes únicamente a usuarios
    que tengan una sesión válida y un rol reconocido.
    """
    pass
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
