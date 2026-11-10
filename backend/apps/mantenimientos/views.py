from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.usuarios.permissions import EsUsuarioAutenticado
from apps.usuarios.roles import (
    ROL_ADMINISTRADOR,
    ROL_TECNICO,
)

from .serializers import MantenimientoSerializer
from .services import (
    listar_mantenimientos,
    obtener_mantenimiento,
)


class MantenimientoListView(APIView):

    permission_classes = [EsUsuarioAutenticado]

    def get(self, request):

        rol = request.session.get("usuario_rol")

        if rol not in (ROL_ADMINISTRADOR, ROL_TECNICO):
            return Response(
                {
                    "detail": (
                        "No tienes permisos para consultar "
                        "los mantenimientos."
                    )
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        mantenimientos = listar_mantenimientos()

        return Response(
            MantenimientoSerializer(
                mantenimientos,
                many=True,
            ).data
        )


class MantenimientoDetailView(APIView):

    permission_classes = [EsUsuarioAutenticado]

    def get(self, request, id_mantenimiento):

        rol = request.session.get("usuario_rol")

        if rol not in (ROL_ADMINISTRADOR, ROL_TECNICO):
            return Response(
                {
                    "detail": (
                        "No tienes permisos para consultar "
                        "este mantenimiento."
                    )
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        mantenimiento = obtener_mantenimiento(
            id_mantenimiento
        )

        if mantenimiento is None:
            return Response(
                {
                    "detail": "Mantenimiento no encontrado."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            MantenimientoSerializer(
                mantenimiento
            ).data
        )
