import datetime
from unittest.mock import Mock, patch

from django.http import HttpResponse
from django.test import RequestFactory, SimpleTestCase, override_settings
from django.contrib.sessions.middleware import SessionMiddleware

from config.views import inicio
from apps.usuarios.models import Usuario
from apps.usuarios.views import LoginView, LogoutView, PerfilView, RegisterView


def add_session(request):
    """Agrega una sesión real de Django al RequestFactory request."""
    middleware = SessionMiddleware(lambda request: None)
    middleware.process_request(request)
    request.session.save()
    return request


@override_settings(SESSION_ENGINE="django.contrib.sessions.backends.signed_cookies")
class TestLoginView(SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @patch("apps.usuarios.views.render")
    def test_login_get_muestra_formulario(self, mock_render):
        request = add_session(self.factory.get("/usuarios/login/"))

        mock_render.return_value = HttpResponse(status=200)
        response = LoginView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        mock_render.assert_called_once()
        render_request, template_name = mock_render.call_args.args
        self.assertIs(render_request._request, request)
        self.assertEqual(template_name, "login.html")

    def test_login_get_con_sesion_de_usuario_redirige_al_index(self):
        request = add_session(self.factory.get("/usuarios/login/"))
        request.session["usuario_id"] = 10
        request.session["usuario_rol"] = 2

        response = LoginView.as_view()(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/")

    def test_login_redirige_admin_y_tecnico_a_sus_paneles(self):
        for rol, url in ((1, "/admin-home/"), (3, "/tecnico/")):
            with self.subTest(rol=rol):
                request = add_session(self.factory.get("/usuarios/login/"))
                request.session["usuario_id"] = 10
                request.session["usuario_rol"] = rol

                response = LoginView.as_view()(request)

                self.assertEqual(response.status_code, 302)
                self.assertEqual(response.url, url)

    @patch("config.views.listar_equipos", return_value=[])
    @patch("config.views.render")
    def test_index_autenticado_renderiza_index_para_usuario(
        self,
        mock_render,
        _mock_listar_equipos,
    ):
        request = add_session(self.factory.get("/"))
        request.session["usuario_id"] = 10
        request.session["usuario_rol"] = 2
        mock_render.return_value = HttpResponse(status=200)

        response = inicio(request)

        self.assertEqual(response.status_code, 200)
        mock_render.assert_called_once_with(
            request,
            "index.html",
            {"equipos": []},
        )

    @patch("apps.usuarios.views.render")
    def test_login_post_sin_datos_muestra_error(self, mock_render):
        request = add_session(
            self.factory.post(
                "/usuarios/login/",
                data={"email": "", "clave": ""},
            )
        )

        mock_render.return_value = HttpResponse(status=200)
        response = LoginView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        mock_render.assert_called_once()
        render_request, template_name, context = mock_render.call_args.args
        self.assertIs(render_request._request, request)
        self.assertEqual(template_name, "login.html")
        self.assertEqual(context, {"error": "Debes ingresar correo y contraseña."})

    @patch("apps.usuarios.views.render")
    @patch("apps.usuarios.views.autenticar_usuario", return_value=None)
    def test_login_con_credenciales_invalidas(self, mock_auth, mock_render):
        request = add_session(
            self.factory.post(
                "/usuarios/login/",
                data={
                    "email": "nadie@example.com",
                    "clave": "incorrecta",
                },
            )
        )

        mock_render.return_value = HttpResponse(status=200)
        response = LoginView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        mock_render.assert_called_once()
        render_request, template_name, context = mock_render.call_args.args
        self.assertIs(render_request._request, request)
        self.assertEqual(template_name, "login.html")
        self.assertEqual(context, {"error": "Correo o contraseña incorrectos."})
        mock_auth.assert_called_once_with(
            "nadie@example.com",
            "incorrecta",
        )

    @patch("apps.usuarios.views.autenticar_usuario")
    def test_login_exitoso_crea_sesion_y_redirige(self, mock_auth):
        usuario = Mock()
        usuario.id_usuario = 7
        usuario.nombre_usuario = "usuario1"
        usuario.email = "usuario@example.com"
        usuario.id_rol_fk = 2
        mock_auth.return_value = usuario

        request = add_session(
            self.factory.post(
                "/usuarios/login/",
                data={
                    "email": "usuario@example.com",
                    "clave": "Password123",
                },
            )
        )

        response = LoginView.as_view()(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/")
        self.assertEqual(request.session["usuario_id"], 7)
        self.assertEqual(request.session["usuario_nombre"], "usuario1")
        self.assertEqual(
            request.session["usuario_email"],
            "usuario@example.com",
        )


class TestRegisterView(SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.data = {
            "nombres": "Juan",
            "apellidos": "Pérez",
            "numero_tel": "3001234567",
            "nombre_usuario": "juanp",
            "email": "juan@example.com",
            "fecha_nacimiento": "2005-05-20",
            "clave": "Password123",
        }

    @patch("apps.usuarios.views.render")
    def test_register_sin_datos_muestra_error(self, mock_render):
        request = self.factory.post(
            "/usuarios/register/",
            data={},
        )

        mock_render.return_value = Mock(status_code=200)
        response = RegisterView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        mock_render.assert_called_once_with(
            request, "login.html", {"error_registro": "Todos los campos son obligatorios."}
        )

    @patch("apps.usuarios.views.render")
    @patch("apps.usuarios.views.Usuario.objects.filter")
    def test_register_rechaza_correo_duplicado(self, mock_filter, mock_render):
        mock_filter.return_value.exists.return_value = True

        request = self.factory.post(
            "/usuarios/register/",
            data=self.data,
        )

        mock_render.return_value = Mock(status_code=200)
        response = RegisterView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        mock_render.assert_called_once_with(
            request, "login.html", {"error_registro": "El correo ya está registrado."}
        )
        mock_filter.assert_called_once_with(
            email="juan@example.com"
        )

    @patch("apps.usuarios.views.render")
    @patch("apps.usuarios.views.Usuario.objects.create")
    @patch("apps.usuarios.views.Usuario.objects.filter")
    def test_register_rechaza_usuario_duplicado(
        self,
        mock_filter,
        mock_create,
        mock_render,
    ):
        email_query = Mock()
        email_query.exists.return_value = False

        user_query = Mock()
        user_query.exists.return_value = True

        mock_filter.side_effect = [email_query, user_query]

        request = self.factory.post(
            "/usuarios/register/",
            data=self.data,
        )

        mock_render.return_value = Mock(status_code=200)
        response = RegisterView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        mock_render.assert_called_once_with(
            request, "login.html", {"error_registro": "El nombre de usuario ya está registrado."}
        )
        mock_create.assert_not_called()

    @patch("apps.usuarios.views.Usuario.objects.create")
    @patch("apps.usuarios.views.Usuario.objects.filter")
    def test_register_guarda_usuario_directamente(
        self,
        mock_filter,
        mock_create,
    ):
        query = Mock()
        query.exists.return_value = False
        mock_filter.return_value = query

        request = self.factory.post(
            "/usuarios/register/",
            data=self.data,
        )

        response = RegisterView.as_view()(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/usuarios/login/")

        mock_create.assert_called_once_with(
            nombres="Juan",
            apellidos="Pérez",
            numero_tel="3001234567",
            nombre_usuario="juanp",
            email="juan@example.com",
            fecha_nacimiento="2005-05-20",
            clave="Password123",
            id_rol_fk=2,
        )

    @patch("apps.usuarios.views.render")
    @patch("apps.usuarios.views.Usuario.objects.create")
    @patch("apps.usuarios.views.Usuario.objects.filter")
    def test_register_muestra_error_si_falla_la_base_de_datos(
        self,
        mock_filter,
        mock_create,
        mock_render,
    ):
        query = Mock()
        query.exists.return_value = False
        mock_filter.return_value = query
        mock_create.side_effect = Exception("DB error")

        request = self.factory.post(
            "/usuarios/register/",
            data=self.data,
        )

        mock_render.return_value = Mock(status_code=200)
        response = RegisterView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        mock_render.assert_called_once_with(
            request, "login.html", {"error_registro": "Error al guardar el usuario: DB error"}
        )


class TestLogoutView(SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_logout_elimina_la_sesion_y_redirige(self):
        request = add_session(self.factory.get("/usuarios/logout/"))
        request.session["usuario_id"] = 99
        request.session["usuario_nombre"] = "usuario"

        response = LogoutView.as_view()(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/usuarios/login/")
        self.assertIsNone(request.session.get("usuario_id"))


class TestPerfilView(SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @patch("apps.usuarios.views.obtener_usuario", return_value=None)
    def test_perfil_usuario_no_encontrado(self, mock_get):
        request = self.factory.get("/usuarios/perfil/99/")

        response = PerfilView.as_view()(request, id_usuario=99)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.data,
            {"detail": "Usuario no encontrado."},
        )
        mock_get.assert_called_once_with(99)

    @patch("apps.usuarios.views.obtener_usuario")
    def test_perfil_usuario_encontrado(self, mock_get):
        usuario = Mock()
        usuario.id_usuario = 7
        usuario.nombres = "Juan"
        usuario.apellidos = "Pérez"
        usuario.numero_tel = "3001234567"
        usuario.nombre_usuario = "juanp"
        usuario.email = "juan@example.com"
        usuario.fecha_nacimiento = datetime.date(2005, 5, 20)
        usuario.id_rol_fk = 2
        mock_get.return_value = usuario

        request = self.factory.get("/usuarios/perfil/7/")

        response = PerfilView.as_view()(request, id_usuario=7)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id_usuario"], 7)
        self.assertEqual(response.data["email"], "juan@example.com")
        self.assertEqual(response.data["id_rol_fk"], 2)
