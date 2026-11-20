from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import IntegrityError, transaction
from django.views.decorators.http import require_POST

from apps.usuarios.roles import (
    ROL_ADMINISTRADOR,
    ROL_USUARIO,
    ROL_TECNICO,
)

from .models import TipoEquipo, Ubicacion, Equipo
from .services import listar_equipos, dar_de_baja_equipo


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

    lista_equipos = listar_equipos()

    return render(
        request,
        "equipos.html",
        {
            "equipos": lista_equipos
        }
    )


def equipo_detalle(request, id_equipo):
    if not usuario_autorizado(request):
        return redirect("login")

    equipo = get_object_or_404(
        Equipo.objects.select_related(
            "id_tipo_equipo_fk",
            "id_ubicacion_fk",
        ),
        id_equipo=id_equipo,
    )

    return render(
        request,
        "equipos.html",
        {
            "equipos": [equipo]
        }
    )


@require_POST
def gestionar_equipo(request):
    if not request.session.get("usuario_id"):
        return redirect("login")

    if request.session.get("usuario_rol") != ROL_ADMINISTRADOR:
        messages.error(
            request,
            "No tienes permisos para gestionar equipos."
        )
        return redirect("equipos_admin")

    accion = request.POST.get("accion")

    if accion == "eliminar":
        id_equipo = request.POST.get("id_equipo")

        if not id_equipo or not dar_de_baja_equipo(id_equipo):
            messages.error(request, "No se encontró el equipo.")
        else:
            messages.success(
                request,
                "El equipo fue dado de baja. Su historial se conservó."
            )

        return redirect("equipos_admin")

    if accion not in ("agregar", "actualizar"):
        messages.error(request, "La operación solicitada no es válida.")
        return redirect("equipos_admin")

    codigo = request.POST.get("codigo", "").strip()
    tipo_id = request.POST.get("tipo_equipo")
    fecha_compra = request.POST.get("fecha_compra") or None
    ubicacion_id = request.POST.get("ubicacion") or None
    estado = request.POST.get("estado_general", "operativo")

    if not codigo or not tipo_id:
        messages.error(request, "El código y el tipo de equipo son obligatorios.")
        return redirect("equipos_admin")

    if estado not in ("operativo", "en_reparacion"):
        messages.error(request, "El estado seleccionado no es válido.")
        return redirect("equipos_admin")

    if not TipoEquipo.objects.filter(pk=tipo_id).exists():
        messages.error(request, "El tipo de equipo seleccionado no existe.")
        return redirect("equipos_admin")

    if ubicacion_id and not Ubicacion.objects.filter(pk=ubicacion_id).exists():
        messages.error(request, "La ubicación seleccionada no existe.")
        return redirect("equipos_admin")

    try:
        with transaction.atomic():
            if accion == "agregar":
                Equipo.objects.create(
                    codigo=codigo,
                    id_tipo_equipo_fk_id=tipo_id,
                    fecha_compra=fecha_compra,
                    id_ubicacion_fk_id=ubicacion_id,
                    estado_general=estado,
                )

                messages.success(request, "Equipo registrado correctamente.")

            else:
                id_equipo = request.POST.get("id_equipo")
                equipo = Equipo.objects.filter(
                    pk=id_equipo
                ).first()

                if equipo is None:
                    messages.error(request, "No se encontró el equipo.")
                    return redirect("equipos_admin")

                if equipo.estado_general == "dado_de_baja":
                    messages.error(
                        request,
                        "No se puede modificar un equipo que ya fue dado de baja."
                    )
                    return redirect("equipos_admin")

                equipo.codigo = codigo
                equipo.id_tipo_equipo_fk_id = tipo_id
                equipo.fecha_compra = fecha_compra
                equipo.id_ubicacion_fk_id = ubicacion_id
                equipo.estado_general = estado

                equipo.save()

                messages.success(request, "Equipo actualizado correctamente.")

    except IntegrityError:
        messages.error(
            request,
            "No se pudo guardar el equipo. Comprueba que el código no esté repetido."
        )

    return redirect("equipos_admin")

