from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PiezaSerializer, TipoPiezaSerializer
from .services import (
    listar_piezas,
    listar_tipos_pieza,
    obtener_pieza,
)


class PiezaListView(APIView):

    def get(self, request):

        piezas = listar_piezas()

        return Response(
            PiezaSerializer(
                piezas,
                many=True
            ).data
        )


class TipoPiezaListView(APIView):

    def get(self, request):

        tipos = listar_tipos_pieza()
        
        return Response(
            TipoPiezaSerializer(
                tipos,
                many=True
            ).data
        )


class PiezaDetailView(APIView):

    def get(self, request, id_pieza):

        pieza = obtener_pieza(id_pieza)

        if pieza is None:
            return Response(
                {"detail": "Pieza no encontrada."},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            PiezaSerializer(pieza).data
        )