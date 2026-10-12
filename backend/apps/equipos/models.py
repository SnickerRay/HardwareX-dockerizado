from django.db import models


class TipoEquipo(models.Model):
    id_tipo_equipo = models.AutoField(primary_key=True)
    nombre_tipo = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = "tipo_equipo"

    def __str__(self):
        return self.nombre_tipo


class Ubicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    sede = models.CharField(max_length=100)
    salon = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = "ubicacion"

    def __str__(self):
        return f"{self.sede} - {self.salon}"


class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=100)

    id_tipo_equipo_fk = models.ForeignKey(
        TipoEquipo,
        on_delete=models.DO_NOTHING,
        db_column="id_tipo_equipo_fk",
        related_name="equipos"
    )

    fecha_compra = models.DateField(
        null=True,
        blank=True
    )

    id_ubicacion_fk = models.ForeignKey(
        Ubicacion,
        on_delete=models.DO_NOTHING,
        db_column="id_ubicacion_fk",
        null=True,
        blank=True,
        related_name="equipos"
    )

    estado_general = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = "equipo"

    def __str__(self):
        return self.codigo