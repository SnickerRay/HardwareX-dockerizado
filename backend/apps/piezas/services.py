from .models import Pieza, TipoPieza


def listar_piezas():
    return Pieza.objects.all()


def listar_tipos_pieza():
    return TipoPieza.objects.all()


def obtener_pieza(id_pieza):
    try:
        return Pieza.objects.get(id_pieza=id_pieza)
    except Pieza.DoesNotExist:
        return None