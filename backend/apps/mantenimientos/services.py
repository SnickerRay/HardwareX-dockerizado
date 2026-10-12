from .models import Mantenimiento


def listar_mantenimientos():
    return Mantenimiento.objects.all()


def obtener_mantenimiento(id_mantenimiento):

    try:
        return Mantenimiento.objects.get(
            id_mantenimiento=id_mantenimiento
        )

    except Mantenimiento.DoesNotExist:
        return None