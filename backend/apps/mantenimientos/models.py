from django.db import models


class Mantenimiento(models.Model):
    id_mantenimiento = models.AutoField(
        primary_key=True
    )

    class Meta:
        managed = False
        db_table = "mantenimiento"