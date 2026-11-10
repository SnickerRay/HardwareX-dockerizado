from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.usuarios.permissions import EsUsuarioAutenticado
from apps.usuarios.roles import (
    ROL_ADMINISTRADOR,
    ROL_TECNICO,
)

from .serializers import PiezaSerializer, TipoPiezaSerializer
from .services import (
    listar_piezas,
    listar_tipos_pieza,
    obtener_pieza,
)


class PiezaListView(APIView):

    permission_classes = [EsUsuarioAutenticado]

    def get(self, request):

        rol = request.session.get("usuario_rol")

        if rol not in (ROL_ADMINISTRADOR, ROL_TECNICO):
            return Response(
                {
                    "detail": (
                        "No tienes permisos para consultar "
                        "el inventario de piezas."
                    )
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        piezas = listar_piezas()

        return Response(
            PiezaSerializer(
                piezas,
                many=True,
            ).data
        )


class TipoPiezaListView(APIView):

    permission_classes = [EsUsuarioAutenticado]

    def get(self, request):

        rol = request.session.get("usuario_rol")

        if rol not in (ROL_ADMINISTRADOR, ROL_TECNICO):
            return Response(
                {
                    "detail": (
                        "No tienes permisos para consultar "
                        "los tipos de piezas."
                    )
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        tipos = listar_tipos_pieza()

        return Response(
            TipoPiezaSerializer(
                tipos,
                many=True,
            ).data
        )


class PiezaDetailView(APIView):

    permission_classes = [EsUsuarioAutenticado]

    def get(self, request, id_pieza):

        rol = request.session.get("usuario_rol")

        if rol not in (ROL_ADMINISTRADOR, ROL_TECNICO):
            return Response(
                {
                    "detail": (
                        "No tienes permisos para consultar "
                        "esta pieza."
                    )
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        pieza = obtener_pieza(id_pieza)

        if pieza is None:
            return Response(
                {"detail": "Pieza no encontrada."},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            PiezaSerializer(pieza).data
        )
