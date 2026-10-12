from .models import Reporte


def listar_reportes():
    return Reporte.objects.all()


def obtener_reporte(id_reporte):

    try:
        return Reporte.objects.get(
            id_reporte=id_reporte
        )

    except Reporte.DoesNotExist:
        return None