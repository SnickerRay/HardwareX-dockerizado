from rest_framework.permissions import BasePermission


class MantenimientoPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated