from pathlib import Path
import re
from unittest.mock import patch

from django.test import RequestFactory, SimpleTestCase
from django.urls import reverse

from apps.solicitudes.views import (
    AceptarAsignacionFormView,
    AsignarTecnicoFormView,
)


BASE_DIR = Path(__file__).resolve().parents[2]
LOGIN_TEMPLATE = BASE_DIR / "frontend" / "templates" / "login.html"
EQUIPOS_TEMPLATE = BASE_DIR / "frontend" / "templates" / "equipos.html"
TECNICOS_TEMPLATE = BASE_DIR / "frontend" / "templates" / "tecnicos_admin.html"
HISTORIAL_ADMIN_TEMPLATE = BASE_DIR / "frontend" / "templates" / "historial_admin.html"
TECNICO_TEMPLATE = BASE_DIR / "frontend" / "templates" / "tecnico.html"
MANTENIMIENTOS_TEMPLATE = BASE_DIR / "frontend" / "templates" / "mantenimientos.html"
REPORTES_TEMPLATE = BASE_DIR / "frontend" / "templates" / "reportes_tecnico.html"
GENERAL_REPORTES_TEMPLATE = BASE_DIR / "frontend" / "templates" / "reportes.html"
REPAIR_FORM_TEMPLATE = BASE_DIR / "frontend" / "templates" / "repair_form.html"
EQUIPMENT_DETAIL_TEMPLATE = BASE_DIR / "frontend" / "templates" / "equipos.html"
LOGIN_JS = BASE_DIR / "frontend" / "static" / "js" / "login.js"


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
            r'<button[^>]*type="submit"[^>]*>\s*Registrarse\s*</button>',
            re.IGNORECASE | re.DOTALL,
        )
        self.assertRegex(self.login_html, pattern)

    def test_login_muestra_error_y_control_de_contrasena(self):
        self.assertIn('id="show-password"', self.login_html)
        self.assertIn('name="email"', self.login_html)
        self.assertIn('name="clave"', self.login_html)
        self.assertIn('role="alert">{{ error }}</p>', self.login_html)


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


class TestAdminTechniciansFrontend(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.technicians_html = TECNICOS_TEMPLATE.read_text(encoding="utf-8")
        cls.history_html = HISTORIAL_ADMIN_TEMPLATE.read_text(encoding="utf-8")

    def test_tecnicos_admin_usa_datos_reales_y_permita_asignar(self):
        self.assertIn("{% tecnicos_admin_panel as tecnicos %}", self.technicians_html)
        self.assertIn("{% solicitudes_asignables as solicitudes %}", self.technicians_html)
        self.assertIn('name="id_solicitud"', self.technicians_html)
        self.assertIn('name="id_tecnico"', self.technicians_html)
        self.assertIn('name="origen" value="tecnicos_admin"', self.technicians_html)
        self.assertIn("Asignar solicitud", self.technicians_html)

    def test_historial_muestra_asignaciones_reales(self):
        self.assertIn("{% historial_asignaciones as asignaciones %}", self.history_html)
        self.assertIn("asignacion.id_solicitud_fk.id_solicitud", self.history_html)
        self.assertIn("asignacion.id_tecnico_fk.nombres", self.history_html)

    @patch("apps.solicitudes.views.messages.success")
    @patch("apps.solicitudes.views.asignar_tecnico")
    def test_asignacion_desde_tecnicos_regresa_al_panel(
        self,
        mock_asignar_tecnico,
        _mock_mensaje,
    ):
        request = RequestFactory().post(
            "/solicitudes-api/asignar-tecnico/",
            {
                "id_solicitud": "12",
                "id_tecnico": "4",
                "origen": "tecnicos_admin",
            },
        )
        request.session = {"usuario_id": 1, "usuario_rol": 1}

        response = AsignarTecnicoFormView.as_view()(request)

        mock_asignar_tecnico.assert_called_once_with(12, 4)
        self.assertRedirects(
            response,
            reverse("tecnicos_admin"),
            fetch_redirect_response=False,
        )


class TestTechnicianFrontend(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.dashboard_html = TECNICO_TEMPLATE.read_text(encoding="utf-8")
        cls.equipment_html = EQUIPMENT_DETAIL_TEMPLATE.read_text(encoding="utf-8")
        cls.maintenance_html = MANTENIMIENTOS_TEMPLATE.read_text(encoding="utf-8")
        cls.reports_html = REPORTES_TEMPLATE.read_text(encoding="utf-8")
        cls.general_reports_html = GENERAL_REPORTES_TEMPLATE.read_text(encoding="utf-8")
        cls.form_html = REPAIR_FORM_TEMPLATE.read_text(encoding="utf-8")

    def test_dashboard_tecnico_usa_listas_reales_y_limites(self):
        self.assertIn("{% dashboard_tecnico as panel_tecnico %}", self.dashboard_html)
        self.assertIn("panel_tecnico.solicitudes", self.dashboard_html)
        self.assertIn('action="{% url \'aceptar_asignacion\' %}"', self.dashboard_html)
        self.assertIn("panel_tecnico.equipos", self.dashboard_html)
        self.assertIn("panel_tecnico.mantenimientos", self.dashboard_html)
        self.assertIn('href="/equipos/">Ver más...', self.dashboard_html)

    def test_paginas_tecnicas_muestran_asignaciones_y_mantenimientos_reales(self):
        self.assertIn("{% equipos_tecnico_asignados as equipos_tecnico %}", self.equipment_html)
        self.assertIn('class="technician-equipment-dialog"', self.equipment_html)
        self.assertIn("{% mantenimientos_tecnico as mantenimientos_tecnico_lista %}", self.maintenance_html)
        self.assertIn("mantenimiento.fecha_fin", self.maintenance_html)

    def test_reportes_reutiliza_el_formulario_de_tres_pasos(self):
        self.assertIn('{% include "repair_form.html" %}', self.reports_html)
        self.assertIn('id="repair-form"', self.form_html)
        self.assertIn('id="wizard-progress"', self.form_html)
        self.assertIn('id="summary-device"', self.form_html)
        self.assertIn('id="submit-button"', self.form_html)
        self.assertIn("Equipos arreglados", self.general_reports_html)

    @patch("apps.solicitudes.views.messages.success")
    @patch("apps.solicitudes.views.aceptar_asignacion")
    def test_tecnico_acepta_su_asignacion_y_regresa_al_dashboard(
        self,
        mock_aceptar,
        _mock_mensaje,
    ):
        request = RequestFactory().post(
            "/solicitudes-api/aceptar-asignacion/",
            {"id_asignacion": "17"},
        )
        request.session = {"usuario_id": 4, "usuario_rol": 3}

        response = AceptarAsignacionFormView.as_view()(request)

        mock_aceptar.assert_called_once_with(17, 4)
        self.assertRedirects(
            response,
            reverse("tecnico"),
            fetch_redirect_response=False,
        )
