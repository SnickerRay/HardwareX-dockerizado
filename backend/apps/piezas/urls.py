from django.urls import path

from .views import (
    PiezaDetailView,
    PiezaListView,
    TipoPiezaListView,
)

urlpatterns = [
    path(
        "",
        PiezaListView.as_view(),
        name="piezas_api",
    ),

    path(
        "tipos/",
        TipoPiezaListView.as_view(),
        name="tipos_pieza_api",
    ),

    path(
        "<int:id_pieza>/",
        PiezaDetailView.as_view(),
        name="pieza_detail_api",
    ),
]