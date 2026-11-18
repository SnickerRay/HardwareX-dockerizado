HEAD
from django.shortcuts import render, get_object_or_404
=======
from django.shortcuts import render, get_object_or_404, redirect

from apps.usuarios.roles import (
    ROL_ADMINISTRADOR,
    ROL_USUARIO,
    ROL_TECNICO,
)
035ab46f93a09b1663ac2b8f0c1ff71d737b9042

from .models import Equipo
from .services import listar_equipos


HEAD
def equipos(request):
=======
ROLES_PERMITIDOS = (
    ROL_ADMINISTRADOR,
    ROL_USUARIO,
    ROL_TECNICO,
)


def usuario_autorizado(request):
    usuario_id = request.session.get("usuario_id")
    rol = request.session.get("usuario_rol")

    return bool(
        usuario_id
        and rol in ROLES_PERMITIDOS
    )


def equipos(request):
    if not usuario_autorizado(request):
        return redirect("login")

035ab46f93a09b1663ac2b8f0c1ff71d737b9042
    lista_equipos = listar_equipos()

    return render(
        request,
        "equipos.html",
        {
            "equipos": lista_equipos
        }
    )


def equipo_detalle(request, id_equipo):
HEAD
    equipo = get_object_or_404(
        Equipo.objects.select_related(
            "id_tipo_equipo_fk",
            "id_ubicacion_fk"
        ),
        id_equipo=id_equipo
=======
    if not usuario_autorizado(request):
        return redirect("login")

    equipo = get_object_or_404(
        Equipo.objects.select_related(
            "id_tipo_equipo_fk",
            "id_ubicacion_fk",
        ),
        id_equipo=id_equipo,
035ab46f93a09b1663ac2b8f0c1ff71d737b9042
    )

    return render(
        request,
        "equipos.html",
        {
            "equipos": [equipo]
        }
HEAD
    )
=======
    )
035ab46f93a09b1663ac2b8f0c1ff71d737b9042
