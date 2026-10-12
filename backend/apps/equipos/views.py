from django.shortcuts import render, get_object_or_404

from .models import Equipo
from .services import listar_equipos


def equipos(request):
    lista_equipos = listar_equipos()

    return render(
        request,
        "equipos.html",
        {
            "equipos": lista_equipos
        }
    )


def equipo_detalle(request, id_equipo):
    equipo = get_object_or_404(
        Equipo.objects.select_related(
            "id_tipo_equipo_fk",
            "id_ubicacion_fk"
        ),
        id_equipo=id_equipo
    )

    return render(
        request,
        "equipos.html",
        {
            "equipos": [equipo]
        }
    )