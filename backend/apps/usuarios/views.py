from django.contrib.auth import logout
from django.shortcuts import redirect, render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Usuario
from .services import autenticar_usuario, obtener_usuario


# ==========================================
# LOGIN
# ==========================================

class LoginView(APIView):

    def get(self, request):

        if request.session.get("usuario_id"):
            return redirect("inicio")

        return render(
            request,
            "login.html"
        )

    def post(self, request):

        email = request.POST.get("email", "").strip()
        clave = request.POST.get("clave", "").strip()

        if not email or not clave:

            return render(
                request,
                "login.html",
                {
                    "error": "Debes ingresar correo y contraseña."
                }
            )

        usuario = autenticar_usuario(
            email,
            clave
        )

        if usuario is None:

            return render(
                request,
                "login.html",
                {
                    "error": "Correo o contraseña incorrectos."
                }
            )

        request.session["usuario_id"] = usuario.id_usuario
        request.session["usuario_nombre"] = usuario.nombre_usuario
        request.session["usuario_email"] = usuario.email

        request.session.set_expiry(
            60 * 60 * 8
        )

        return redirect("inicio")


# ==========================================
# REGISTRO
# ==========================================

class RegisterView(APIView):

    def get(self, request):

        return render(
            request,
            "login.html"
        )

    def post(self, request):

        nombres = request.POST.get(
            "nombres",
            ""
        ).strip()

        apellidos = request.POST.get(
            "apellidos",
            ""
        ).strip()

        numero_tel = request.POST.get(
            "numero_tel",
            ""
        ).strip()

        nombre_usuario = request.POST.get(
            "nombre_usuario",
            ""
        ).strip()

        email = request.POST.get(
            "email",
            ""
        ).strip()

        fecha_nacimiento = request.POST.get(
            "fecha_nacimiento",
            ""
        ).strip()

        clave = request.POST.get(
            "clave",
            ""
        ).strip()


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
            clave
        ]):

            return render(
                request,
                "login.html",
                {
                    "error_registro":
                    "Todos los campos son obligatorios."
                }
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
        # ==========================================

        try:

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

            return render(
                request,
                "login.html",
                {
                    "error_registro":
                    f"Error al guardar el usuario: {error}"
                }
            )


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