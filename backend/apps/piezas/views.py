from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

<<<<<<< HEAD
=======
from apps.usuarios.permissions import EsUsuarioAutenticado
from apps.usuarios.roles import (
    ROL_ADMINISTRADOR,
    ROL_TECNICO,
)

>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
from .serializers import PiezaSerializer, TipoPiezaSerializer
from .services import (
    listar_piezas,
    listar_tipos_pieza,
    obtener_pieza,
)


class PiezaListView(APIView):

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
                        "el inventario de piezas."
                    )
                },
                status=status.HTTP_403_FORBIDDEN,
            )

>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
        piezas = listar_piezas()

        return Response(
            PiezaSerializer(
                piezas,
<<<<<<< HEAD
                many=True
=======
                many=True,
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
            ).data
        )


class TipoPiezaListView(APIView):

<<<<<<< HEAD
    def get(self, request):

        tipos = listar_tipos_pieza()
        
        return Response(
            TipoPiezaSerializer(
                tipos,
                many=True
=======
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
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
            ).data
        )


class PiezaDetailView(APIView):

<<<<<<< HEAD
    def get(self, request, id_pieza):

=======
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

>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
        pieza = obtener_pieza(id_pieza)

        if pieza is None:
            return Response(
                {"detail": "Pieza no encontrada."},
<<<<<<< HEAD
                status=status.HTTP_404_NOT_FOUND
=======
                status=status.HTTP_404_NOT_FOUND,
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
            )

        return Response(
            PiezaSerializer(pieza).data
<<<<<<< HEAD
        )
=======
        )
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
