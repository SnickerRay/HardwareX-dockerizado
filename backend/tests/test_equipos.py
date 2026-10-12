from unittest.mock import Mock, patch

from django.test import RequestFactory, SimpleTestCase

from apps.equipos.views import equipo_detalle, equipos


class TestEquiposViews(SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @patch("apps.equipos.views.render")
    @patch("apps.equipos.views.listar_equipos")
    def test_equipos_envia_lista_a_la_template(self, mock_listar, mock_render):
        equipo = Mock()
        equipo.id_equipo = 1
        equipo.codigo = "EQ-001"
        mock_listar.return_value = [equipo]
        mock_render.return_value = Mock(status_code=200)

        request = self.factory.get("/equipos/")
        response = equipos(request)

        self.assertEqual(response.status_code, 200)
        mock_listar.assert_called_once_with()
        mock_render.assert_called_once_with(
            request,
            "equipos.html",
            {"equipos": [equipo]},
        )

    @patch("apps.equipos.views.render")
    @patch("apps.equipos.views.get_object_or_404")
    def test_detalle_equipo_envia_un_solo_equipo(self, mock_get, mock_render):
        equipo = Mock()
        equipo.id_equipo = 15
        equipo.codigo = "EQ-015"
        mock_get.return_value = equipo
        mock_render.return_value = Mock(status_code=200)

        request = self.factory.get("/equipos/15/")
        response = equipo_detalle(request, id_equipo=15)

        self.assertEqual(response.status_code, 200)
        mock_get.assert_called_once()
        mock_render.assert_called_once_with(
            request,
            "equipos.html",
            {"equipos": [equipo]},
        )
