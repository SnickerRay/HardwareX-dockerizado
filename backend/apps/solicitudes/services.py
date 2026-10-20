from django.db import transaction
from django.db.models import Count
from django.utils import timezone

from .models import Asignacion, Solicitud
from apps.usuarios.models import Usuario

ESTADOS_ASIGNACION_ACTIVOS = ("asignado", "en_curso")
PRIORIDADES_URGENTES = ("alta", "urgente", "importante")


def listar_solicitudes():
    return Solicitud.objects.all()


def obtener_solicitud(id_solicitud):
    try:
        return Solicitud.objects.get(
            id_solicitud=id_solicitud
        )
    except Solicitud.DoesNotExist:
        return None


def listar_solicitudes_pendientes():
    return (
        Solicitud.objects
        .filter(estado="pendiente")
        .exclude(
            asignaciones__estado_asignacion__in=ESTADOS_ASIGNACION_ACTIVOS
        )
        .select_related("id_usuario_fk", "id_equipo_fk__id_tipo_equipo_fk")
        .order_by("-fecha_solicitud")
        .distinct()
    )


def listar_solicitudes_urgentes(limite=5):
    return (
        Solicitud.objects
        .filter(
            prioridad_usuario__in=PRIORIDADES_URGENTES,
            estado__in=("pendiente", "en_proceso"),
        )
        .select_related("id_usuario_fk", "id_equipo_fk")
        .order_by("-fecha_solicitud")[:limite]
    )


def contar_solicitudes_pendientes():
    return Solicitud.objects.filter(estado="pendiente").count()


def actividad_solicitudes_por_dia(fecha_inicio, fecha_fin):
    return (
        Solicitud.objects
        .filter(fecha_solicitud__date__range=(fecha_inicio, fecha_fin))
        .values("fecha_solicitud__date")
        .annotate(total=Count("id_solicitud"))
        .order_by("fecha_solicitud__date")
    )


@transaction.atomic
def asignar_tecnico(id_solicitud, id_tecnico):
    solicitud = (
        Solicitud.objects
        .select_for_update()
        .get(id_solicitud=id_solicitud)
    )
    tecnico = Usuario.objects.get(id_usuario=id_tecnico)

    if tecnico.id_rol_fk != 3:
        raise ValueError("El usuario seleccionado no tiene rol de técnico.")

    if solicitud.estado != "pendiente":
        raise ValueError("La solicitud ya no está pendiente.")

    if solicitud.asignaciones.filter(
        estado_asignacion__in=ESTADOS_ASIGNACION_ACTIVOS
    ).exists():
        raise ValueError("La solicitud ya tiene un técnico asignado.")

    Asignacion.objects.create(
        id_solicitud_fk=solicitud,
        id_tecnico_fk=tecnico,
        prioridad_asignada=solicitud.prioridad_usuario,
        fecha_asignacion=timezone.now(),
        estado_asignacion="asignado",
    )
    solicitud.estado = "en_proceso"
    solicitud.save(update_fields=["estado"])

    return solicitud