from django.db import models


class Solicitud(models.Model):
    id_solicitud = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = "solicitud"