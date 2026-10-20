from datetime import timedelta

from django import template
from django.db.models import Count, Q
from django.utils import timezone

from apps.equipos.services import listar_equipos
from apps.piezas.services import listar_piezas
from apps.solicitudes.models import Asignacion, Solicitud
from apps.solicitudes.services import (
    actividad_solicitudes_por_dia,
    contar_solicitudes_pendientes,
    listar_solicitudes_pendientes,
    listar_solicitudes_urgentes,
)
from apps.usuarios.services import listar_tecnicos

register = template.Library()

ROL_ADMINISTRADOR = 1
ROL_TECNICO = 3
ESTADOS_ASIGNACION_ACTIVOS = ("asignado", "en_curso")
ESTADOS_TRABAJO_TECNICO = ESTADOS_ASIGNACION_ACTIVOS + ("finalizado",)


@register.simple_tag
def admin_dashboard():
    equipos = listar_equipos()
    hoy = timezone.localdate()
    fechas = [hoy - timedelta(days=offset) for offset in range(6, -1, -1)]
    actividad_por_fecha = {
        fila["fecha_solicitud__date"]: fila["total"]
        for fila in actividad_solicitudes_por_dia(fechas[0], fechas[-1])
    }
    actividad = [actividad_por_fecha.get(fecha, 0) for fecha in fechas]
    max_actividad = max(actividad, default=0)
    max_grafica = max(max_actividad, 1)
    puntos = [
        f"{18 + index * 47},{112 - round(valor / max_grafica * 92)}"
        for index, valor in enumerate(actividad)
    ]
    promedio_anterior = sum(actividad[:-1]) / 6

    if actividad[-1] >= 3 and actividad[-1] > promedio_anterior * 2:
        estado_actividad, clase_actividad = "Incremento grave", "critical"
    elif actividad[-1] > promedio_anterior:
        estado_actividad, clase_actividad = "Actividad en aumento", "attention"
    else:
        estado_actividad, clase_actividad = "Actividad estable", "stable"

    abreviaturas_dia = ("lun", "mar", "mié", "jue", "vie", "sáb", "dom")
    return {
        "total_equipos": equipos.count(),
        "total_piezas": listar_piezas().count(),
        "total_solicitudes": contar_solicitudes_pendientes(),
        "equipos_por_tipo": (
            equipos.values("id_tipo_equipo_fk__nombre_tipo")
            .annotate(total=Count("id_equipo"))
            .order_by("id_tipo_equipo_fk__nombre_tipo")[:3]
        ),
        "solicitudes": listar_solicitudes_urgentes(),
        "actividad": actividad,
        "puntos_actividad": " ".join(puntos),
        "fechas_actividad": [
            {
                "dia": abreviaturas_dia[fecha.weekday()],
                "fecha": fecha.strftime("%d/%m"),
            }
            for fecha in fechas
        ],
        "max_actividad": max_actividad,
        "estado_actividad": estado_actividad,
        "clase_actividad": clase_actividad,
    }


@register.simple_tag(takes_context=True)
def solicitudes_panel(context):
    request = context["request"]
    rol = request.session.get("usuario_rol")

    if rol == ROL_ADMINISTRADOR:
        solicitudes = listar_solicitudes_pendientes()
        tecnicos = listar_tecnicos()
    elif rol == ROL_TECNICO:
        solicitudes = (
            Solicitud.objects
            .filter(
                asignaciones__id_tecnico_fk_id=request.session["usuario_id"],
                asignaciones__estado_asignacion__in=ESTADOS_ASIGNACION_ACTIVOS,
            )
            .select_related(
                "id_usuario_fk",
                "id_equipo_fk__id_tipo_equipo_fk",
            )
            .order_by("-fecha_solicitud")
            .distinct()
        )
        tecnicos = ()
    else:
        solicitudes = ()
        tecnicos = ()

    return {"solicitudes": solicitudes, "tecnicos": tecnicos}


@register.simple_tag
def tecnicos_admin_panel():
    return (
        listar_tecnicos()
        .annotate(
            trabajos_asignados=Count(
                "asignaciones_tecnico",
                filter=Q(
                    asignaciones_tecnico__estado_asignacion__in=ESTADOS_TRABAJO_TECNICO
                ),
            ),
            trabajos_pendientes=Count(
                "asignaciones_tecnico",
                filter=Q(
                    asignaciones_tecnico__estado_asignacion__in=ESTADOS_ASIGNACION_ACTIVOS
                ),
            ),
        )
    )


@register.simple_tag
def solicitudes_asignables():
    return listar_solicitudes_pendientes()


@register.simple_tag
def historial_asignaciones():
    return (
        Asignacion.objects
        .select_related("id_solicitud_fk", "id_tecnico_fk")
        .order_by("-fecha_asignacion", "-id_asignacion")
    )
