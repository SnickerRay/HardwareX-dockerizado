from rest_framework import serializers
from .models import Equipo


class EquipoSerializer(serializers.ModelSerializer):

    tipo_equipo = serializers.CharField(
        source="id_tipo_equipo_fk.nombre_tipo",
        read_only=True
    )

    ubicacion = serializers.SerializerMethodField()

    class Meta:
        model = Equipo

        fields = [
            "id_equipo",
            "codigo",
            "tipo_equipo",
            "ubicacion",
            "estado_general",
        ]

    def get_ubicacion(self, obj):

        if obj.id_ubicacion_fk:
            return f"{obj.id_ubicacion_fk.sede} - {obj.id_ubicacion_fk.salon}"

        return "Sin ubicación"