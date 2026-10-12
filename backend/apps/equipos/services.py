from .models import Equipo, TipoEquipo, Ubicacion


def listar_equipos():
    return (
        Equipo.objects
        .select_related(
            "id_tipo_equipo_fk",
            "id_ubicacion_fk"
        )
        .order_by("codigo")
    )


def obtener_equipo(id_equipo):

    try:
        return (
            Equipo.objects
            .select_related(
                "id_tipo_equipo_fk",
                "id_ubicacion_fk"
            )
            .get(id_equipo=id_equipo)
        )

    except Equipo.DoesNotExist:
        return None


def listar_tipos_equipo():
    return TipoEquipo.objects.all().order_by("nombre_tipo")


def listar_ubicaciones():
    return Ubicacion.objects.all().order_by("sede", "salon")