from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ReporteSerializer
from .services import (
    listar_reportes,
    obtener_reporte,
)


class ReporteListView(APIView):

    def get(self, request):

        reportes = listar_reportes()

        return Response(
            ReporteSerializer(
                reportes,
                many=True
            ).data
        )


class ReporteDetailView(APIView):

    def get(self, request, id_reporte):

        reporte = obtener_reporte(id_reporte)

        if reporte is None:
            return Response(
                {"detail": "Reporte no encontrado."},
                status=404
            )

        return Response(
            ReporteSerializer(reporte).data
        )