from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import MantenimientoSerializer
from .services import (
    listar_mantenimientos,
    obtener_mantenimiento,
)


class MantenimientoListView(APIView):

    def get(self, request):

        mantenimientos = listar_mantenimientos()

        return Response(
            MantenimientoSerializer(
                mantenimientos,
                many=True
            ).data
        )


class MantenimientoDetailView(APIView):

    def get(self, request, id_mantenimiento):

        mantenimiento = obtener_mantenimiento(
            id_mantenimiento
        )

        if mantenimiento is None:
            return Response(
                {
                    "detail":
                    "Mantenimiento no encontrado."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            MantenimientoSerializer(
                mantenimiento
            ).data
        )