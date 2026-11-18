from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
<<<<<<< HEAD
from rest_framework.response import Response
from rest_framework.views import APIView

=======

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.usuarios.permissions import EsUsuarioAutenticado
from apps.usuarios.roles import (
    ROL_ADMINISTRADOR,
    ROL_TECNICO,
)

>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
from .serializers import ReporteSerializer
from .services import (
    listar_reportes,
    obtener_reporte,
)


class ReporteTecnicoPageView(View):

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get("usuario_id"):
            return redirect("login")
<<<<<<< HEAD
        if request.session.get("usuario_rol") != 3:
            return redirect("inicio")
=======

        if request.session.get("usuario_rol") not in (
            ROL_ADMINISTRADOR,
            ROL_TECNICO,
        ):
            return redirect("inicio")

>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, "reportes_tecnico.html")

    def post(self, request):
        messages.error(
            request,
<<<<<<< HEAD
            "El formulario está listo visualmente, pero el guardado de reportes técnicos "
            "aún no está disponible porque la base de datos no tiene una tabla de reportes.",
=======
            "El formulario está listo visualmente, pero el guardado "
            "de reportes técnicos aún no está disponible porque "
            "la base de datos no tiene una tabla de reportes.",
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
        )
        return redirect("reportes_tecnico")


class ReporteListView(APIView):

<<<<<<< HEAD
    def get(self, request):

=======
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

>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
        reportes = listar_reportes()

        return Response(
            ReporteSerializer(
                reportes,
<<<<<<< HEAD
                many=True
=======
                many=True,
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
            ).data
        )


class ReporteDetailView(APIView):

<<<<<<< HEAD
    def get(self, request, id_reporte):

=======
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

>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
        reporte = obtener_reporte(id_reporte)

        if reporte is None:
            return Response(
                {"detail": "Reporte no encontrado."},
<<<<<<< HEAD
                status=404
=======
                status=status.HTTP_404_NOT_FOUND,
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
            )

        return Response(
            ReporteSerializer(reporte).data
<<<<<<< HEAD
        )
=======
        )
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
