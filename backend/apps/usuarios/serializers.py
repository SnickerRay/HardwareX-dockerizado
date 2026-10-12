from rest_framework import serializers
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            "id_usuario",
            "nombres",
            "apellidos",
            "numero_tel",
            "nombre_usuario",
            "email",
            "fecha_nacimiento",
            "id_rol_fk",
        ]


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    clave = serializers.CharField(write_only=True)