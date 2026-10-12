from rest_framework.permissions import BasePermission


class EsUsuarioAutenticado(BasePermission):
    """
    Permiso base para usuarios autenticados.
    """

    message = "Debes estar autenticado para realizar esta acción."

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)