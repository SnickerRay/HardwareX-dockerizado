<<<<<<< HEAD
=======

>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
from rest_framework import serializers

from .models import Solicitud


class SolicitudSerializer(serializers.ModelSerializer):

    class Meta:
        model = Solicitud
<<<<<<< HEAD
        fields = ("id_solicitud",)
=======
        fields = (
            "id_solicitud",
            "id_equipo_fk",
            "descripcion",
            "prioridad_usuario",
            "fecha_solicitud",
            "estado",
        )
        read_only_fields = (
            "id_solicitud",
            "fecha_solicitud",
            "estado",
        )
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
