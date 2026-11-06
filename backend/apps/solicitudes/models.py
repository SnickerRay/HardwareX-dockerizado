from django.db import models

from apps.equipos.models import Equipo
from apps.usuarios.models import Usuario


class Solicitud(models.Model):
    id_solicitud = models.AutoField(primary_key=True)
    id_usuario_fk = models.ForeignKey(
        Usuario,
        on_delete=models.DO_NOTHING,
        db_column="id_usuario_fk",
        related_name="solicitudes_reportadas",
    )
    id_equipo_fk = models.ForeignKey(
        Equipo,
        on_delete=models.DO_NOTHING,
        db_column="id_equipo_fk",
        related_name="solicitudes",
    )
    descripcion = models.TextField()
    prioridad_usuario = models.CharField(max_length=10)
    fecha_solicitud = models.DateTimeField()
    estado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = "solicitud_reparacion"

    def __str__(self):
        return f"Solicitud #{self.id_solicitud}"


class Asignacion(models.Model):
    id_asignacion = models.AutoField(primary_key=True)
    id_solicitud_fk = models.ForeignKey(
        Solicitud,
        on_delete=models.DO_NOTHING,
        db_column="id_solicitud_fk",
        related_name="asignaciones",
    )
    id_tecnico_fk = models.ForeignKey(
        Usuario,
        on_delete=models.DO_NOTHING,
        db_column="id_tecnico_fk",
        related_name="asignaciones_tecnico",
    )
    prioridad_asignada = models.CharField(max_length=10)
    fecha_asignacion = models.DateTimeField()
    estado_asignacion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = "asignacion"
