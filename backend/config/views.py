from django.shortcuts import render

from apps.equipos.services import (
    listar_equipos,
    listar_tipos_equipo,
    listar_ubicaciones,
)
from apps.usuarios.services import listar_tecnicos
from apps.reportes.services import listar_reportes
from apps.solicitudes.services import listar_solicitudes


def inicio(request):
    equipos = listar_equipos()
    return render(request, "index.html", {"equipos": equipos})


def login_page(request):
    return render(request, "login.html")


def historial(request):
    return render(request, "historial.html")


def historial_admin(request):
    return render(request, "historial_admin.html")


def equipos(request):
    lista_equipos = listar_equipos()
    return render(request, "equipos.html", {"equipos": lista_equipos})


def equipos_admin(request):
    return render(
        request,
        "equipos_admin.html",
        {
            "equipos": listar_equipos(),
            "tipos_equipo": listar_tipos_equipo(),
            "ubicaciones": listar_ubicaciones(),
        }
    )


def mantenimientos(request):
    return render(request, "mantenimientos.html")


def perfil(request):
    return render(request, "perfil.html")


def perfil_tecnico(request):
    return render(request, "perfil_tecnico.html")


def piezas(request):
    return render(request, "piezas.html")


def reportes(request):
    return render(request, "reportes.html")


def reportes_recientes(request):
    return render(
        request,
        "reportes_recientes.html",
        {
            "reportes": listar_reportes(),
            "tecnicos": listar_tecnicos(),
        }
    )


def solicitudes(request):
    return render(request, "solicitudes.html")


def tecnico(request):
    return render(request, "tecnico.html")


def tecnicos_admin(request):
    return render(request, "tecnicos_admin.html")


def asignaciones(request):
    return render(request, "asignaciones.html")


def admin_home(request):
    return render(
        request,
        "admin_home.html",
        {"solicitudes": listar_solicitudes()}
    )


def crear_solicitud(request):
    return render(request, "crear_solicitud.html")