from django.urls import path

from .views import ( MantenimientoDetailView, MantenimientoListView,)

urlpatterns = [
    path(
        "",
        MantenimientoListView.as_view(),
        name="mantenimientos_api",
    ),

    path(
        "<int:id_mantenimiento>/",
        MantenimientoDetailView.as_view(),
        name="mantenimiento_detail_api",
    ),
]