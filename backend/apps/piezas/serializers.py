from rest_framework import serializers

from .models import Pieza, TipoPieza


class TipoPiezaSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoPieza
        fields = "__all__"


class PiezaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pieza
        fields = "__all__"