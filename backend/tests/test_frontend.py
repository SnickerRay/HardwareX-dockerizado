from pathlib import Path
import re

from django.test import SimpleTestCase


BASE_DIR = Path(__file__).resolve().parents[2]
LOGIN_TEMPLATE = BASE_DIR.parent / "frontend" / "templates" / "login.html"
EQUIPOS_TEMPLATE = BASE_DIR.parent / "frontend" / "templates" / "equipos.html"
LOGIN_JS = BASE_DIR.parent / "frontend" / "static" / "js" / "login.js"


class TestLoginFrontend(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.login_html = LOGIN_TEMPLATE.read_text(encoding="utf-8")
        cls.login_js = LOGIN_JS.read_text(encoding="utf-8")

    def test_formulario_registro_apunta_a_register(self):
        self.assertIn(
            'action="{% url \'register\' %}"',
            self.login_html,
        )

    def test_formulario_login_apunta_a_login(self):
        self.assertIn(
            'action="{% url \'login\' %}"',
            self.login_html,
        )

    def test_login_y_register_tienen_identificadores_correctos(self):
        self.assertIn('id="loginForm"', self.login_html)
        self.assertIn('id="registerForm"', self.login_html)
        self.assertIn('id="login"', self.login_html)
        self.assertIn('id="register"', self.login_html)
        self.assertIn('id="container"', self.login_html)

    def test_javascript_activa_la_animacion_de_registro(self):
        self.assertIn("right-panel-active", self.login_js)
        self.assertIn("registerButton.addEventListener", self.login_js)
        self.assertIn("loginButton.addEventListener", self.login_js)

    def test_registro_debe_enviarse_con_submit(self):
        pattern = re.compile(
            r'<button[^>]*type="submit"[^>]*>\s*Register\s*</button>',
            re.IGNORECASE | re.DOTALL,
        )
        self.assertRegex(self.login_html, pattern)


class TestEquiposFrontend(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.html = EQUIPOS_TEMPLATE.read_text(encoding="utf-8")

    def test_template_recibe_contexto_de_equipos(self):
        self.assertIn("{% for equipo in equipos %}", self.html)

    def test_template_muestra_campos_principales(self):
        self.assertIn("equipo.id_equipo", self.html)
        self.assertIn("equipo.codigo", self.html)
        self.assertIn("equipo.id_tipo_equipo_fk.nombre_tipo", self.html)
        self.assertIn("equipo.id_ubicacion_fk.salon", self.html)

    def test_template_tiene_estado_vacio(self):
        self.assertIn("No hay equipos registrados.", self.html)
