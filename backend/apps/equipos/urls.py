from django.urls import path

from .views import equipos, equipo_detalle


urlpatterns = [
    path("", equipos, name="equipos"),
    path("<int:id_equipo>/", equipo_detalle, name="equipo_detalle"),
]