
from unittest.mock import Mock, patch

from django.test import RequestFactory, SimpleTestCase
from rest_framework import status

from apps.solicitudes.models import Asignacion
from apps.solicitudes.views import (
    AceptarAsignacionFormView,
    SolicitudDetailView,
    SolicitudListView,
)
from apps.usuarios.roles import (
    ROL_ADMINISTRADOR,
    ROL_USUARIO,
    ROL_TECNICO,
)


class TestPermisosSolicitudes(SimpleTestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def crear_request(self, url, usuario_id=None, rol=None):
        request = self.factory.get(url)
        request.session = {}

        if usuario_id is not None:
            request.session["usuario_id"] = usuario_id

        if rol is not None:
            request.session["usuario_rol"] = rol

        return request

    def test_usuario_sin_sesion_no_puede_consultar_solicitudes(self):
        request = self.crear_request("/solicitudes-api/")

        response = SolicitudListView.as_view()(request)

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN,
        )

    @patch("apps.solicitudes.views.SolicitudSerializer")
    @patch("apps.solicitudes.views.Solicitud.objects.select_related")
    def test_usuario_solo_consulta_sus_solicitudes(
        self,
        mock_select_related,
        mock_serializer,
    ):
        solicitudes = Mock()
        mock_select_related.return_value = solicitudes
        solicitudes.filter.return_value = solicitudes
        solicitudes.order_by.return_value = []

        mock_serializer.return_value.data = []

        request = self.crear_request(
            "/solicitudes-api/",
            usuario_id=10,
            rol=ROL_USUARIO,
        )

        response = SolicitudListView.as_view()(request)

        solicitudes.filter.assert_called_once_with(
            id_usuario_fk_id=10
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch("apps.solicitudes.views.SolicitudSerializer")
    @patch("apps.solicitudes.views.Solicitud.objects.select_related")
    def test_administrador_puede_consultar_todas_las_solicitudes(
        self,
        mock_select_related,
        mock_serializer,
    ):
        solicitudes = Mock()
        mock_select_related.return_value = solicitudes
        solicitudes.order_by.return_value = []

        mock_serializer.return_value.data = []

        request = self.crear_request(
            "/solicitudes-api/",
            usuario_id=1,
            rol=ROL_ADMINISTRADOR,
        )

        response = SolicitudListView.as_view()(request)

        solicitudes.filter.assert_not_called()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch("apps.solicitudes.views.SolicitudSerializer")
    @patch("apps.solicitudes.views.Solicitud.objects.select_related")
    def test_tecnico_puede_consultar_todas_las_solicitudes(
        self,
        mock_select_related,
        mock_serializer,
    ):
        solicitudes = Mock()
        mock_select_related.return_value = solicitudes
        solicitudes.order_by.return_value = []

        mock_serializer.return_value.data = []

        request = self.crear_request(
            "/solicitudes-api/",
            usuario_id=20,
            rol=ROL_TECNICO,
        )

        response = SolicitudListView.as_view()(request)

        solicitudes.filter.assert_not_called()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch("apps.solicitudes.views.SolicitudSerializer")
    @patch("apps.solicitudes.views.Solicitud.objects.select_related")
    def test_usuario_no_puede_consultar_solicitud_de_otro_usuario(
        self,
        mock_select_related,
        mock_serializer,
    ):
        solicitudes = Mock()
        mock_select_related.return_value = solicitudes
        solicitudes.filter.return_value = solicitudes
        solicitudes.first.return_value = None

        request = self.crear_request(
            "/solicitudes-api/50/",
            usuario_id=10,
            rol=ROL_USUARIO,
        )

        response = SolicitudDetailView.as_view()(
            request,
            id_solicitud=50,
        )

        solicitudes.filter.assert_any_call(
            id_usuario_fk_id=10
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )

    @patch("apps.solicitudes.views.messages.error")
    @patch("apps.solicitudes.views.aceptar_asignacion")
    def test_tecnico_no_puede_aceptar_asignacion_de_otro_tecnico(
        self,
        mock_aceptar,
        mock_error,
    ):
        mock_aceptar.side_effect = Asignacion.DoesNotExist

        request = self.factory.post(
            "/solicitudes-api/aceptar-asignacion/",
            {"id_asignacion": "50"},
        )
        request.session = {
            "usuario_id": 20,
            "usuario_rol": ROL_TECNICO,
        }

        response = AceptarAsignacionFormView.as_view()(request)

        mock_aceptar.assert_called_once_with(50, 20)
        mock_error.assert_called_once()

        self.assertEqual(response.status_code, 302)
