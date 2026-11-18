<<<<<<< HEAD
=======

import hashlib
import logging
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
import re
from datetime import date

from django.contrib.auth import logout
<<<<<<< HEAD
=======
from django.contrib.auth.hashers import make_password
from django.core.cache import cache
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import redirect, render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Usuario
from .services import autenticar_usuario, obtener_usuario
<<<<<<< HEAD
=======
from .permissions import EsUsuarioAutenticado, EsUsuarioPropietario
from .roles import (
    ROL_ADMINISTRADOR,
    ROL_USUARIO,
    ROL_TECNICO,
)


# ==========================================
# CONFIGURACION Y REGISTRO DE ERRORES
# ==========================================

logger = logging.getLogger(__name__)

MAX_INTENTOS_LOGIN = 3
TIEMPO_BLOQUEO_LOGIN = 15 * 60
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042


# ==========================================
# LOGIN
# ==========================================

class LoginView(APIView):

    @staticmethod
    def _destino_por_rol(request):
        rol = request.session.get("usuario_rol")
<<<<<<< HEAD
        if rol == 1:
            return redirect("admin_home")
        if rol == 2:
            return redirect("inicio")
        if rol == 3:
            return redirect("tecnico")
        return redirect("login")

=======

        if rol == ROL_ADMINISTRADOR:
            return redirect("admin_home")

        if rol == ROL_USUARIO:
            return redirect("inicio")

        if rol == ROL_TECNICO:
            return redirect("tecnico")

        return redirect("login")

    @staticmethod
    def _obtener_clave_bloqueo(email, ip):
        identificador = f"{ip}:{email.lower().strip()}"

        identificador_hash = hashlib.sha256(
            identificador.encode("utf-8")
        ).hexdigest()

        return f"login_intentos_{identificador_hash}"

    @staticmethod
    def _registrar_intento_fallido(clave_cache):
        if cache.add(
            clave_cache,
            1,
            timeout=TIEMPO_BLOQUEO_LOGIN,
        ):
            return 1

        try:
            intentos = cache.incr(clave_cache)

        except ValueError:
            cache.set(
                clave_cache,
                1,
                timeout=TIEMPO_BLOQUEO_LOGIN,
            )
            return 1

        cache.touch(
            clave_cache,
            timeout=TIEMPO_BLOQUEO_LOGIN,
        )

        return intentos

>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
    def get(self, request):

        if request.session.get("usuario_id"):
            return self._destino_por_rol(request)

        return render(
            request,
<<<<<<< HEAD
            "login.html"
=======
            "login.html",
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
        )

    def post(self, request):

        email = request.POST.get("email", "").strip()
        clave = request.POST.get("clave", "").strip()

        if not email or not clave:
<<<<<<< HEAD

=======
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
            return render(
                request,
                "login.html",
                {
                    "error": "Debes ingresar correo y contraseña."
<<<<<<< HEAD
                }
            )

        usuario = autenticar_usuario(
            email,
            clave
        )

        if usuario is None:

=======
                },
            )

        # ==========================================
        # IDENTIFICAR CORREO E IP
        # ==========================================

        ip = request.META.get(
            "REMOTE_ADDR",
            "desconocida",
        )

        clave_cache = self._obtener_clave_bloqueo(
            email,
            ip,
        )

        # ==========================================
        # VERIFICAR SI ESTA BLOQUEADO
        # ==========================================

        intentos = cache.get(
            clave_cache,
            0,
        )

        if intentos >= MAX_INTENTOS_LOGIN:
            return render(
                request,
                "login.html",
                {
                    "error": "Correo o contraseña incorrectos."
                },
            )

        # ==========================================
        # AUTENTICAR USUARIO
        # ==========================================

        try:
            usuario = autenticar_usuario(
                email,
                clave,
            )

        except Exception:
            logger.exception(
                "Error inesperado durante la autenticación."
            )

            return render(
                request,
                "login.html",
                {
                    "error": (
                        "No fue posible iniciar sesión. "
                        "Inténtalo nuevamente."
                    )
                },
            )

        if usuario is None:

            self._registrar_intento_fallido(
                clave_cache,
            )

>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
            return render(
                request,
                "login.html",
                {
                    "error": "Correo o contraseña incorrectos."
<<<<<<< HEAD
                }
            )

        request.session["usuario_id"] = usuario.id_usuario
        request.session["usuario_nombre"] = usuario.nombre_usuario
        request.session["usuario_email"] = usuario.email
        # El rol se toma del registro autenticado, nunca del formulario.
=======
                },
            )

        # ==========================================
        # LOGIN CORRECTO: REINICIAR INTENTOS
        # ==========================================

        cache.delete(clave_cache)

        # ==========================================
        # CREAR SESION
        # ==========================================

        request.session.cycle_key()

        request.session["usuario_id"] = usuario.id_usuario
        request.session["usuario_nombre"] = usuario.nombre_usuario
        request.session["usuario_email"] = usuario.email
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
        request.session["usuario_rol"] = usuario.id_rol_fk

        request.session.set_expiry(
            60 * 60 * 8
        )

        return self._destino_por_rol(request)


# ==========================================
# REGISTRO
# ==========================================

class RegisterView(APIView):

    def get(self, request):

        return render(
            request,
<<<<<<< HEAD
            "login.html"
=======
            "login.html",
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
        )

    def post(self, request):

        nombres = request.POST.get(
            "nombres",
<<<<<<< HEAD
            ""
=======
            "",
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
        ).strip()

        apellidos = request.POST.get(
            "apellidos",
<<<<<<< HEAD
            ""
=======
            "",
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
        ).strip()

        numero_tel = request.POST.get(
            "numero_tel",
<<<<<<< HEAD
            ""
=======
            "",
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
        ).strip()

        nombre_usuario = request.POST.get(
            "nombre_usuario",
<<<<<<< HEAD
            ""
=======
            "",
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
        ).strip()

        email = request.POST.get(
            "email",
<<<<<<< HEAD
            ""
=======
            "",
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
        ).strip()

        fecha_nacimiento = request.POST.get(
            "fecha_nacimiento",
<<<<<<< HEAD
            ""
=======
            "",
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
        ).strip()

        clave = request.POST.get(
            "clave",
<<<<<<< HEAD
            ""
        ).strip()


=======
            "",
        ).strip()

>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
        # ==========================================
        # VALIDAR CAMPOS
        # ==========================================

        if not all([
            nombres,
            apellidos,
            numero_tel,
            nombre_usuario,
            email,
            fecha_nacimiento,
<<<<<<< HEAD
            clave
        ]):

=======
            clave,
        ]):
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
            return render(
                request,
                "login.html",
                {
<<<<<<< HEAD
                    "error_registro":
                    "Todos los campos son obligatorios."
                }
            )

        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s'-]{2,100}", nombres):
            return render(
                request,
                "login.html",
                {"error_registro": "Ingresa nombres válidos (solo letras y espacios)."},
            )

        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s'-]{2,100}", apellidos):
            return render(
                request,
                "login.html",
                {"error_registro": "Ingresa apellidos válidos (solo letras y espacios)."},
            )

        if not re.fullmatch(r"[+0-9()\s-]{7,20}", numero_tel):
            return render(
                request,
                "login.html",
                {"error_registro": "Ingresa un número de teléfono válido."},
            )

        if not re.fullmatch(r"[A-Za-z0-9_.-]{3,50}", nombre_usuario):
=======
                    "error_registro": (
                        "Todos los campos son obligatorios."
                    )
                },
            )

        if not re.fullmatch(
            r"[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s'-]{2,100}",
            nombres,
        ):
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
            return render(
                request,
                "login.html",
                {
<<<<<<< HEAD
                    "error_registro":
                    "El usuario debe tener 3-50 caracteres: letras, números, punto, guion o guion bajo."
=======
                    "error_registro": (
                        "Ingresa nombres válidos "
                        "(solo letras y espacios)."
                    )
                },
            )

        if not re.fullmatch(
            r"[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s'-]{2,100}",
            apellidos,
        ):
            return render(
                request,
                "login.html",
                {
                    "error_registro": (
                        "Ingresa apellidos válidos "
                        "(solo letras y espacios)."
                    )
                },
            )

        if not re.fullmatch(
            r"[+0-9()\s-]{7,20}",
            numero_tel,
        ):
            return render(
                request,
                "login.html",
                {
                    "error_registro": (
                        "Ingresa un número de teléfono válido."
                    )
                },
            )

        if not re.fullmatch(
            r"[A-Za-z0-9_.-]{3,50}",
            nombre_usuario,
        ):
            return render(
                request,
                "login.html",
                {
                    "error_registro": (
                        "El usuario debe tener 3-50 caracteres: "
                        "letras, números, punto, guion o guion bajo."
                    )
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
                },
            )

        try:
            validate_email(email)
<<<<<<< HEAD
=======

>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
        except ValidationError:
            return render(
                request,
                "login.html",
<<<<<<< HEAD
                {"error_registro": "Ingresa un correo electrónico válido."},
            )

        try:
            fecha_nacimiento_valida = date.fromisoformat(fecha_nacimiento)
=======
                {
                    "error_registro": (
                        "Ingresa un correo electrónico válido."
                    )
                },
            )

        try:
            fecha_nacimiento_valida = date.fromisoformat(
                fecha_nacimiento,
            )

>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
        except ValueError:
            return render(
                request,
                "login.html",
<<<<<<< HEAD
                {"error_registro": "Ingresa una fecha de nacimiento válida."},
=======
                {
                    "error_registro": (
                        "Ingresa una fecha de nacimiento válida."
                    )
                },
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
            )

        if fecha_nacimiento_valida > date.today():
            return render(
                request,
                "login.html",
<<<<<<< HEAD
                {"error_registro": "La fecha de nacimiento no puede ser futura."},
=======
                {
                    "error_registro": (
                        "La fecha de nacimiento no puede ser futura."
                    )
                },
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
            )

        if len(clave) < 8 or len(clave) > 128:
            return render(
                request,
                "login.html",
<<<<<<< HEAD
                {"error_registro": "La contraseña debe tener entre 8 y 128 caracteres."},
            )

        # ==========================================
        # VALIDAR CORREO
        # ==========================================

        if Usuario.objects.filter(
            email=email
        ).exists():

            return render(
                request,
                "login.html",
                {
                    "error_registro":
                    "El correo ya está registrado."
                }
            )


        # ==========================================
        # VALIDAR USUARIO
        # ==========================================

        if Usuario.objects.filter(
            nombre_usuario=nombre_usuario
        ).exists():

            return render(
                request,
                "login.html",
                {
                    "error_registro":
                    "El nombre de usuario ya está registrado."
                }
            )


        # ==========================================
        # GUARDAR DIRECTAMENTE EN POSTGRESQL
=======
                {
                    "error_registro": (
                        "La contraseña debe tener entre "
                        "8 y 128 caracteres."
                    )
                },
            )

        # ==========================================
        # VALIDAR Y GUARDAR USUARIO
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
        # ==========================================

        try:

<<<<<<< HEAD
            Usuario.objects.create(

                nombres=nombres,

                apellidos=apellidos,

                numero_tel=numero_tel,

                nombre_usuario=nombre_usuario,

                email=email,

                fecha_nacimiento=fecha_nacimiento,

                clave=clave,

                # Rol Usuario
                id_rol_fk=2
            )

        except Exception as error:

            print(
                "ERROR AL GUARDAR USUARIO:"
            )

            print(error)

=======
            if Usuario.objects.filter(email=email).exists():
                return render(
                    request,
                    "login.html",
                    {
                        "error_registro": (
                            "El correo ya está registrado."
                        )
                    },
                )

            if Usuario.objects.filter(
                nombre_usuario=nombre_usuario
            ).exists():
                return render(
                    request,
                    "login.html",
                    {
                        "error_registro": (
                            "El nombre de usuario ya está registrado."
                        )
                    },
                )

            # Guardar usuario con contraseña hasheada.
            Usuario.objects.create(
                nombres=nombres,
                apellidos=apellidos,
                numero_tel=numero_tel,
                nombre_usuario=nombre_usuario,
                email=email,
                fecha_nacimiento=fecha_nacimiento,
                clave=make_password(clave),
                id_rol_fk=ROL_USUARIO,
            )

        except Exception:
            logger.exception(
                "Error inesperado durante el registro de un usuario."
            )

>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
            return render(
                request,
                "login.html",
                {
<<<<<<< HEAD
                    "error_registro":
                    f"Error al guardar el usuario: {error}"
                }
            )


=======
                    "error_registro": (
                        "No fue posible completar el registro. "
                        "Inténtalo nuevamente."
                    )
                },
            )

>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
        # ==========================================
        # REGISTRO CORRECTO
        # ==========================================

        return redirect("login")


# ==========================================
# LOGOUT
# ==========================================

class LogoutView(APIView):

    def get(self, request):

        logout(request)

        return redirect("login")

    def post(self, request):

        logout(request)

        return redirect("login")


# ==========================================
# PERFIL
# ==========================================

class PerfilView(APIView):

<<<<<<< HEAD
    def get(
        self,
        request,
        id_usuario
    ):

        usuario = obtener_usuario(
            id_usuario
        )

        if usuario is None:

            return Response(
                {
                    "detail":
                    "Usuario no encontrado."
                },
                status=404
            )

        return Response(
            {
                "id_usuario":
                    usuario.id_usuario,

                "nombres":
                    usuario.nombres,

                "apellidos":
                    usuario.apellidos,

                "numero_tel":
                    usuario.numero_tel,

                "nombre_usuario":
                    usuario.nombre_usuario,

                "email":
                    usuario.email,

                "fecha_nacimiento":
                    usuario.fecha_nacimiento,

                "id_rol_fk":
                    usuario.id_rol_fk,
            }
        )
=======
    permission_classes = [EsUsuarioAutenticado]

    def get(self, request, id_usuario):

        permiso_propietario = EsUsuarioPropietario()

        if not permiso_propietario.tiene_propiedad(
            request,
            id_usuario,
        ):
            return Response(
                {
                    "detail": (
                        "No tienes permisos para consultar "
                        "este perfil."
                    )
                },
                status=403,
            )

        usuario = obtener_usuario(id_usuario)

        if usuario is None:
            return Response(
                {
                    "detail": "Usuario no encontrado."
                },
                status=404,
            )

        return Response({
            "id_usuario": usuario.id_usuario,
            "nombres": usuario.nombres,
            "apellidos": usuario.apellidos,
            "numero_tel": usuario.numero_tel,
            "nombre_usuario": usuario.nombre_usuario,
            "email": usuario.email,
            "fecha_nacimiento": usuario.fecha_nacimiento,
            "id_rol_fk": usuario.id_rol_fk,
        })
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
