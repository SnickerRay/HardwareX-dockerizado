from django.db import connection, transaction
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
def aceptar_asignacion(id_asignacion, id_tecnico):
    asignacion = (
        Asignacion.objects
        .select_for_update()
        .get(
            id_asignacion=id_asignacion,
            id_tecnico_fk_id=id_tecnico,
            estado_asignacion="asignado",
        )
    )
    asignacion.estado_asignacion = "en_curso"
    asignacion.save(update_fields=["estado_asignacion"])
    return asignacion


def _consultar_detalles_tecnico(
    id_tecnico,
    filtros,
    parametros,
    limite=None,
    solo_completados=False,
):
    clausula_limite = "LIMIT %s" if limite is not None else ""
    if limite is not None:
        parametros.append(limite)
    placeholders = ", ".join(["%s"] * len(filtros))
    if solo_completados:
        join_mantenimiento = """
            JOIN mantenimiento AS mantenimiento
                ON mantenimiento.id_asignacion_fk = a.id_asignacion
        """
        filtro_completados = "AND mantenimiento.fecha_fin IS NOT NULL"
        orden = "mantenimiento.fecha_fin DESC, mantenimiento.id_mantenimiento DESC"
    else:
        join_mantenimiento = """
            LEFT JOIN LATERAL (
                SELECT
                    m.id_mantenimiento,
                    m.tipo,
                    m.fecha_inicio,
                    m.fecha_fin,
                    m.descripcion,
                    m.archivo_ruta
                FROM mantenimiento AS m
                WHERE m.id_asignacion_fk = a.id_asignacion
                ORDER BY m.fecha_inicio DESC, m.id_mantenimiento DESC
                LIMIT 1
            ) AS mantenimiento ON TRUE
        """
        filtro_completados = ""
        orden = "a.fecha_asignacion DESC, a.id_asignacion DESC"
    consulta = f"""
        SELECT
            a.id_asignacion,
            a.fecha_asignacion,
            a.estado_asignacion,
            s.id_solicitud,
            s.descripcion AS motivo_falla,
            e.id_equipo,
            e.codigo,
            e.estado_general,
            tipo.nombre_tipo AS tipo_equipo,
            ubicacion.salon,
            ubicacion.sede,
            mantenimiento.id_mantenimiento,
            mantenimiento.tipo AS tipo_mantenimiento,
            mantenimiento.fecha_inicio,
            mantenimiento.fecha_fin,
            mantenimiento.descripcion AS descripcion_mantenimiento,
            mantenimiento.archivo_ruta
        FROM asignacion AS a
        JOIN solicitud_reparacion AS s
            ON s.id_solicitud = a.id_solicitud_fk
        JOIN equipo AS e
            ON e.id_equipo = s.id_equipo_fk
        LEFT JOIN tipo_equipo AS tipo
            ON tipo.id_tipo_equipo = e.id_tipo_equipo_fk
        LEFT JOIN ubicacion
            ON ubicacion.id_ubicacion = e.id_ubicacion_fk
        {join_mantenimiento}
        WHERE a.id_tecnico_fk = %s
            AND a.estado_asignacion IN ({placeholders})
            {filtro_completados}
        ORDER BY {orden}
        {clausula_limite}
    """
    with connection.cursor() as cursor:
        cursor.execute(consulta, [id_tecnico, *filtros, *parametros])
        nombres_columnas = [columna[0] for columna in cursor.description]
        resultados = [
            dict(zip(nombres_columnas, fila))
            for fila in cursor.fetchall()
        ]

    for resultado in resultados:
        ruta_archivo = (resultado["archivo_ruta"] or "").lower()
        resultado["archivo_es_imagen"] = ruta_archivo.endswith(
            (".png", ".jpg", ".jpeg", ".gif", ".webp")
        )
    return resultados


def listar_equipos_asignados_tecnico(id_tecnico, limite=None):
    return _consultar_detalles_tecnico(
        id_tecnico,
        ("asignado", "en_curso"),
        [],
        limite,
    )


def listar_mantenimientos_completados_tecnico(id_tecnico, limite=None):
    resultados = _consultar_detalles_tecnico(
        id_tecnico,
        ("finalizado",),
        [],
        limite,
        solo_completados=True,
    )
    return resultados


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