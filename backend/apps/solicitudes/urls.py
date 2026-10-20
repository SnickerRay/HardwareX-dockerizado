from django.urls import path

from .views import (
    AsignarTecnicoFormView,
    SolicitudDetailView,
    SolicitudListView,
)

urlpatterns = [
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