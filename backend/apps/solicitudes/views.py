from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SolicitudSerializer
from .services import (
    listar_solicitudes,
    obtener_solicitud,
)


class SolicitudListView(APIView):

    def get(self, request):

        solicitudes = listar_solicitudes()

        return Response(
            SolicitudSerializer(
                solicitudes,
                many=True
            ).data
        )


class SolicitudDetailView(APIView):

    def get(self, request, id_solicitud):

        solicitud = obtener_solicitud(id_solicitud)

        if solicitud is None:
            return Response(
                {"detail": "Solicitud no encontrada."},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            SolicitudSerializer(solicitud).data
        )