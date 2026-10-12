from django.db import models


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    clave = models.CharField(max_length=255)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    numero_tel = models.CharField(max_length=20, null=True, blank=True)
    nombre_usuario = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    id_rol_fk = models.IntegerField()

    class Meta:
        managed = False
        db_table = "usuario"

    def __str__(self):
        return self.nombre_usuario