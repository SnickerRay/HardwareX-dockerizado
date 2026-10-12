from .models import Usuario

ROL_TECNICO = 3  # TODO: confirmar el id real del rol "técnico" en tu base de datos


def autenticar_usuario(email, clave):
    try:
        usuario = Usuario.objects.get(email=email)
    except Usuario.DoesNotExist:
        return None

    if usuario.clave != clave:
        return None

    return usuario


def obtener_usuario(id_usuario):
    try:
        return Usuario.objects.get(id_usuario=id_usuario)
    except Usuario.DoesNotExist:
        return None


def listar_tecnicos():
    return Usuario.objects.filter(id_rol_fk=ROL_TECNICO).order_by("nombres")