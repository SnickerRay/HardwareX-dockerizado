
from apps.usuarios.permissions import (
    EsUsuarioAutenticado,
    EsAdministrador,
    EsTecnico,
    EsUsuarioPropietario,
)


class SolicitudPermission(EsUsuarioAutenticado):
    """
    Permite acceder a las solicitudes únicamente a usuarios
    que tengan una sesión válida y un rol reconocido.
    """
    pass
