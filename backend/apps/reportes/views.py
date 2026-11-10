from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.usuarios.permissions import EsUsuarioAutenticado
from apps.usuarios.roles import (
    ROL_ADMINISTRADOR,
    ROL_TECNICO,
)

from .serializers import ReporteSerializer
from .services import (
    listar_reportes,
    obtener_reporte,
)


class ReporteTecnicoPageView(View):

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get("usuario_id"):
            return redirect("login")

        if request.session.get("usuario_rol") not in (
            ROL_ADMINISTRADOR,
            ROL_TECNICO,
        ):
            return redirect("inicio")

        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, "reportes_tecnico.html")

    def post(self, request):
        messages.error(
            request,
            "El formulario está listo visualmente, pero el guardado "
            "de reportes técnicos aún no está disponible porque "
            "la base de datos no tiene una tabla de reportes.",
        )
        return redirect("reportes_tecnico")


class ReporteListView(APIView):

    permission_classes = [EsUsuarioAutenticado]

    def get(self, request):

        rol = request.session.get("usuario_rol")

        if rol not in (ROL_ADMINISTRADOR, ROL_TECNICO):
            return Response(
                {
                    "detail": (
                        "No tienes permisos para consultar "
                        "los reportes técnicos."
                    )
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        reportes = listar_reportes()

        return Response(
            ReporteSerializer(
                reportes,
                many=True,
            ).data
        )


class ReporteDetailView(APIView):

    permission_classes = [EsUsuarioAutenticado]

    def get(self, request, id_reporte):

        rol = request.session.get("usuario_rol")

        if rol not in (ROL_ADMINISTRADOR, ROL_TECNICO):
            return Response(
                {
                    "detail": (
                        "No tienes permisos para consultar "
                        "este reporte técnico."
                    )
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        reporte = obtener_reporte(id_reporte)

        if reporte is None:
            return Response(
                {"detail": "Reporte no encontrado."},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            ReporteSerializer(reporte).data
        )
