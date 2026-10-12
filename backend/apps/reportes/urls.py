from django.urls import path

from .views import (
    ReporteDetailView,
    ReporteListView,
)

urlpatterns = [
    path(
        "",
        ReporteListView.as_view(),
        name="reportes_api",
    ),

    path(
        "<int:id_reporte>/",
        ReporteDetailView.as_view(),
        name="reporte_detail_api",
    ),
]