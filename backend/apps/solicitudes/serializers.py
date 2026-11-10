
from rest_framework import serializers

from .models import Solicitud


class SolicitudSerializer(serializers.ModelSerializer):

    class Meta:
        model = Solicitud
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
