from django.db import models


class TipoPieza(models.Model):
    id_tipo_pieza = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "tipo_pieza"

    def __str__(self):
        return self.nombre


class Pieza(models.Model):
    id_pieza = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_tipo_pieza_fk = models.IntegerField()

    class Meta:
        managed = False
        db_table = "pieza"

    def __str__(self):
        return self.nombre