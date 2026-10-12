from rest_framework import serializers

from .models import Mantenimiento


class MantenimientoSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = Mantenimiento
        fields = "__all__"