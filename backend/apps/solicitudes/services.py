from .models import Solicitud


def listar_solicitudes():
    return Solicitud.objects.all()


def obtener_solicitud(id_solicitud):
    try:
        return Solicitud.objects.get(
            id_solicitud=id_solicitud
        )
    except Solicitud.DoesNotExist:
        return None