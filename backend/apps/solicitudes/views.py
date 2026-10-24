from django.contrib import messages
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views import View

from apps.usuarios.models import Usuario
from .models import Asignacion, Solicitud
from .serializers import SolicitudSerializer
from .services import (
    aceptar_asignacion,
    asignar_tecnico,
    listar_solicitudes,
    obtener_solicitud,
)


class AceptarAsignacionFormView(View):

    def post(self, request):
        if not request.session.get("usuario_id"):
            return redirect("login")

        if request.session.get("usuario_rol") != 3:
            messages.error(request, "Solo un técnico puede aceptar solicitudes.")
            return redirect("inicio")

        try:
            id_asignacion = int(request.POST.get("id_asignacion", ""))
        except ValueError:
            messages.error(request, "Selecciona una asignación válida.")
            return redirect("tecnico")

        try:
            aceptar_asignacion(
                id_asignacion,
                request.session["usuario_id"],
            )
        except Asignacion.DoesNotExist:
            messages.error(
                request,
                "La solicitud ya no está disponible para aceptar.",
            )
        else:
            messages.success(
                request,
                "La solicitud fue aceptada y pasó a estar en curso.",
            )

        return redirect("tecnico")


class AsignarTecnicoFormView(View):

    def post(self, request):
        if not request.session.get("usuario_id"):
            return redirect("login")

        destino = (
            "tecnicos_admin"
            if request.POST.get("origen") == "tecnicos_admin"
            else "solicitudes"
        )

        if request.session.get("usuario_rol") != 1:
            messages.error(request, "Solo un administrador puede asignar técnicos.")
            return redirect(destino)

        try:
            id_solicitud = int(request.POST.get("id_solicitud", ""))
            id_tecnico = int(request.POST.get("id_tecnico", ""))
        except ValueError:
            messages.error(request, "Selecciona una solicitud y un técnico válidos.")
            return redirect(destino)

        try:
            asignar_tecnico(id_solicitud, id_tecnico)
        except Solicitud.DoesNotExist:
            messages.error(request, "La solicitud ya no está disponible.")
        except Usuario.DoesNotExist:
            messages.error(request, "El técnico seleccionado ya no está disponible.")
        except ValueError as error:
            messages.error(request, str(error))
        else:
            messages.success(request, "El técnico fue asignado correctamente.")

        return redirect(destino)


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