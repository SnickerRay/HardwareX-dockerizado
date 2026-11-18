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
from .serializers import MantenimientoSerializer
from .services import (
    listar_mantenimientos,
    obtener_mantenimiento,
)


class MantenimientoListView(APIView):

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
                        "los mantenimientos."
                    )
                },
                status=status.HTTP_403_FORBIDDEN,
            )

>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
        mantenimientos = listar_mantenimientos()

        return Response(
            MantenimientoSerializer(
                mantenimientos,
<<<<<<< HEAD
                many=True
=======
                many=True,
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
            ).data
        )


class MantenimientoDetailView(APIView):

<<<<<<< HEAD
    def get(self, request, id_mantenimiento):

=======
    permission_classes = [EsUsuarioAutenticado]

    def get(self, request, id_mantenimiento):

        rol = request.session.get("usuario_rol")

        if rol not in (ROL_ADMINISTRADOR, ROL_TECNICO):
            return Response(
                {
                    "detail": (
                        "No tienes permisos para consultar "
                        "este mantenimiento."
                    )
                },
                status=status.HTTP_403_FORBIDDEN,
            )

>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
        mantenimiento = obtener_mantenimiento(
            id_mantenimiento
        )

        if mantenimiento is None:
            return Response(
                {
<<<<<<< HEAD
                    "detail":
                    "Mantenimiento no encontrado."
                },
                status=status.HTTP_404_NOT_FOUND
=======
                    "detail": "Mantenimiento no encontrado."
                },
                status=status.HTTP_404_NOT_FOUND,
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
            )

        return Response(
            MantenimientoSerializer(
                mantenimiento
            ).data
<<<<<<< HEAD
        )
=======
        )
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
