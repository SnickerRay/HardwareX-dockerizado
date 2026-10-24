from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ReporteSerializer
from .services import (
    listar_reportes,
    obtener_reporte,
)


class ReporteTecnicoPageView(View):

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get("usuario_id"):
            return redirect("login")
        if request.session.get("usuario_rol") != 3:
            return redirect("inicio")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, "reportes_tecnico.html")

    def post(self, request):
        messages.error(
            request,
            "El formulario está listo visualmente, pero el guardado de reportes técnicos "
            "aún no está disponible porque la base de datos no tiene una tabla de reportes.",
        )
        return redirect("reportes_tecnico")


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