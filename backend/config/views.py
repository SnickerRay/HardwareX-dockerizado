from functools import wraps

from django.shortcuts import redirect, render

from apps.equipos.services import (
    listar_equipos,
    listar_tipos_equipo,
    listar_ubicaciones,
)
from apps.usuarios.services import listar_tecnicos
from apps.reportes.services import listar_reportes
from apps.solicitudes.services import listar_solicitudes


ROL_ADMINISTRADOR = 1
ROL_USUARIO = 2
ROL_TECNICO = 3


def destino_por_rol(request):
    """Devuelve la pantalla inicial correspondiente al rol de la sesión."""
    rol = request.session.get("usuario_rol")
    if rol == ROL_ADMINISTRADOR:
        return redirect("admin_home")
    if rol == ROL_USUARIO:
        return redirect("inicio")
    if rol == ROL_TECNICO:
        return redirect("tecnico")
    return redirect("login")


def roles_requeridos(*roles):
    """Protege vistas HTML validando el rol almacenado en la sesión del servidor."""
    def decorador(vista):
        @wraps(vista)
        def protegida(request, *args, **kwargs):
            if not request.session.get("usuario_id"):
                return redirect("login")
            rol = request.session.get("usuario_rol")
            if rol not in roles:
                return destino_por_rol(request)
            return vista(request, *args, **kwargs)
        return protegida
    return decorador


def requiere_sesion(vista):
    """Exige una sesión válida sin restringir el rol."""
    @wraps(vista)
    def protegida(request, *args, **kwargs):
        if not request.session.get("usuario_id"):
            return redirect("login")
        return vista(request, *args, **kwargs)
    return protegida


def inicio(request):
    # Conserva la página pública para visitantes, pero dirige a usuarios
    # autenticados a la pantalla adecuada para su rol.
    if (
        request.session.get("usuario_id")
        and request.session.get("usuario_rol") != ROL_USUARIO
    ):
        return destino_por_rol(request)
    equipos = listar_equipos()
    return render(request, "index.html", {"equipos": equipos})


def login_page(request):
    if request.session.get("usuario_id"):
        return destino_por_rol(request)
    return render(request, "login.html")


@requiere_sesion
def historial(request):
    return render(request, "historial.html")


@roles_requeridos(ROL_ADMINISTRADOR)
def historial_admin(request):
    return render(request, "historial_admin.html")


@requiere_sesion
def equipos(request):
    lista_equipos = listar_equipos()
    return render(request, "equipos.html", {"equipos": lista_equipos})


@roles_requeridos(ROL_ADMINISTRADOR)
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


@requiere_sesion
def mantenimientos(request):
    return render(request, "mantenimientos.html")


@requiere_sesion
def perfil(request):
    return render(request, "perfil.html")


@roles_requeridos(ROL_TECNICO)
def perfil_tecnico(request):
    return render(request, "perfil_tecnico.html")


@roles_requeridos(ROL_ADMINISTRADOR)
def piezas(request):
    return render(request, "piezas.html")


@roles_requeridos(ROL_USUARIO, ROL_ADMINISTRADOR)
def reportes(request):
    return render(request, "reportes.html")


@roles_requeridos(ROL_ADMINISTRADOR)
def reportes_recientes(request):
    return render(
        request,
        "reportes_recientes.html",
        {
            "reportes": listar_reportes(),
            "tecnicos": listar_tecnicos(),
        }
    )


@requiere_sesion
def solicitudes(request):
    return render(request, "solicitudes.html")


@roles_requeridos(ROL_TECNICO)
def tecnico(request):
    return render(request, "tecnico.html")


@roles_requeridos(ROL_ADMINISTRADOR)
def tecnicos_admin(request):
    return render(request, "tecnicos_admin.html")


@roles_requeridos(ROL_ADMINISTRADOR)
def asignaciones(request):
    return render(request, "asignaciones.html")


@roles_requeridos(ROL_ADMINISTRADOR)
def admin_home(request):
    return render(
        request,
        "admin_home.html",
        {"solicitudes": listar_solicitudes()}
    )


@roles_requeridos(ROL_USUARIO, ROL_ADMINISTRADOR)
def crear_solicitud(request):
    return render(request, "crear_solicitud.html")
