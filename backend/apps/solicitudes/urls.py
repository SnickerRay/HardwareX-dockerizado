from django.urls import path

from .views import (
    AceptarAsignacionFormView,
    AsignarTecnicoFormView,
    SolicitudDetailView,
    SolicitudListView,
)

urlpatterns = [
    path(
        "aceptar-asignacion/",
        AceptarAsignacionFormView.as_view(),
        name="aceptar_asignacion",
    ),
    path(
        "",
        SolicitudListView.as_view(),
        name="solicitudes_api",
    ),

    path(
        "<int:id_solicitud>/",
        SolicitudDetailView.as_view(),
        name="solicitud_detail_api",
    ),

    path(
        "asignar-tecnico/",
        AsignarTecnicoFormView.as_view(),
        name="asignar_tecnico",
    ),
]