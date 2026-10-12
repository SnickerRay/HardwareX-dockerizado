from django.db import models


class Reporte(models.Model):
    id_reporte = models.AutoField(
        primary_key=True
    )

    class Meta:
        managed = False
        db_table = "reporte"