
from django.urls import path

from .views import equipos, equipo_detalle, gestionar_equipo


urlpatterns = [
    path("", equipos, name="equipos_app"),
    path("<int:id_equipo>/", equipo_detalle, name="equipo_detalle"),
    path("gestionar/", gestionar_equipo, name="gestionar_equipo"),
]
