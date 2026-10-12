from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # FRONTEND
    path("", views.inicio, name="inicio"),
    path("login/", views.login_page, name="login"),
    path("historial/", views.historial, name="historial"),
    path("historial-admin/", views.historial_admin, name="historial_admin"),
    path("equipos/", views.equipos, name="equipos"),
    path("equipos-admin/", views.equipos_admin, name="equipos_admin"),
    path("mantenimientos/", views.mantenimientos, name="mantenimientos"),
    path("perfil/", views.perfil, name="perfil"),
    path("perfil-tecnico/", views.perfil_tecnico, name="perfil_tecnico"),
    path("piezas/", views.piezas, name="piezas"),
    path("reportes/", views.reportes, name="reportes"),
    path("reportes-recientes/", views.reportes_recientes, name="reportes_recientes"),
    path("solicitudes/", views.solicitudes, name="solicitudes"),
    path("tecnico/", views.tecnico, name="tecnico"),
    path("tecnicos-admin/", views.tecnicos_admin, name="tecnicos_admin"),
    path("asignaciones/", views.asignaciones, name="asignaciones"),
    path("admin-home/", views.admin_home, name="admin_home"),
    path("crear-solicitud/", views.crear_solicitud, name="crear_solicitud"),

    # APPS / BACKEND
    path("usuarios/", include("apps.usuarios.urls")),
    path("equipos-api/", include("apps.equipos.urls")),
    path("solicitudes-api/", include("apps.solicitudes.urls")),
    path("piezas-api/", include("apps.piezas.urls")),
    path("mantenimientos-api/", include("apps.mantenimientos.urls")),
    path("reportes-api/", include("apps.reportes.urls")),
]