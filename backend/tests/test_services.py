from unittest.mock import Mock, patch

from django.test import SimpleTestCase

from apps.usuarios.services import (
    autenticar_usuario,
    listar_tecnicos,
    obtener_usuario,
)
from apps.equipos.services import listar_equipos


class TestUsuariosServices(SimpleTestCase):
    @patch("apps.usuarios.services.Usuario.objects.get")
    def test_autenticar_usuario_correcto(self, mock_get):
        usuario = Mock()
        usuario.clave = "Password123"
        mock_get.return_value = usuario

        result = autenticar_usuario(
            "juan@example.com",
            "Password123",
        )

        self.assertIs(result, usuario)
        mock_get.assert_called_once_with(email="juan@example.com")

    @patch("apps.usuarios.services.Usuario.objects.get")
    def test_autenticar_usuario_clave_incorrecta(self, mock_get):
        usuario = Mock()
        usuario.clave = "Password123"
        mock_get.return_value = usuario

        result = autenticar_usuario(
            "juan@example.com",
            "incorrecta",
        )

        self.assertIsNone(result)

    @patch("apps.usuarios.services.Usuario.objects.get")
    def test_obtener_usuario_inexistente(self, mock_get):
        from apps.usuarios.models import Usuario

        mock_get.side_effect = Usuario.DoesNotExist

        result = obtener_usuario(999)

        self.assertIsNone(result)

    @patch("apps.usuarios.services.Usuario.objects.filter")
    def test_listar_tecnicos_filtra_por_rol_3_y_ordena(self, mock_filter):
        queryset = Mock()
        queryset.order_by.return_value = ["tecnico"]
        mock_filter.return_value = queryset

        result = listar_tecnicos()

        mock_filter.assert_called_once_with(id_rol_fk=3)
        queryset.order_by.assert_called_once_with("nombres")
        self.assertEqual(result, ["tecnico"])


class TestEquiposServices(SimpleTestCase):
    @patch("apps.equipos.services.Equipo.objects.all")
    def test_listar_equipos_ordena_por_id(self, mock_all):
        queryset = Mock()
        queryset.order_by.return_value = ["equipo1", "equipo2"]
        mock_all.return_value = queryset

        result = listar_equipos()

        mock_all.assert_called_once_with()
        queryset.order_by.assert_called_once_with("id_equipo")
        self.assertEqual(result, ["equipo1", "equipo2"])
