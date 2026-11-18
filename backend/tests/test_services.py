from unittest.mock import Mock, patch

<<<<<<< HEAD
from django.test import SimpleTestCase

=======
from django.contrib.auth.hashers import check_password, make_password
from django.test import SimpleTestCase

from apps.usuarios.roles import ROL_TECNICO
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
from apps.usuarios.services import (
    autenticar_usuario,
    listar_tecnicos,
    obtener_usuario,
)
from apps.equipos.services import listar_equipos
from apps.solicitudes.services import contar_solicitudes_pendientes


class TestUsuariosServices(SimpleTestCase):
<<<<<<< HEAD
    @patch("apps.usuarios.services.Usuario.objects.get")
    def test_autenticar_usuario_correcto(self, mock_get):
=======

    @patch("apps.usuarios.services.Usuario.objects.get")
    def test_autenticar_usuario_correcto_con_clave_antigua(self, mock_get):
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
        usuario = Mock()
        usuario.clave = "Password123"
        mock_get.return_value = usuario

        result = autenticar_usuario(
            "juan@example.com",
            "Password123",
        )

        self.assertIs(result, usuario)
<<<<<<< HEAD
        mock_get.assert_called_once_with(email="juan@example.com")
=======
        self.assertNotEqual(usuario.clave, "Password123")
        self.assertTrue(
            check_password("Password123", usuario.clave)
        )
        usuario.save.assert_called_once_with(
            update_fields=["clave"]
        )

    @patch("apps.usuarios.services.Usuario.objects.get")
    def test_autenticar_usuario_correcto_con_clave_hasheada(self, mock_get):
        usuario = Mock()
        usuario.clave = make_password("Password123")
        hash_original = usuario.clave
        mock_get.return_value = usuario

        result = autenticar_usuario(
            "juan@example.com",
            "Password123",
        )

        self.assertIs(result, usuario)
        self.assertEqual(usuario.clave, hash_original)
        usuario.save.assert_not_called()
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042

    @patch("apps.usuarios.services.Usuario.objects.get")
    def test_autenticar_usuario_clave_incorrecta(self, mock_get):
        usuario = Mock()
<<<<<<< HEAD
        usuario.clave = "Password123"
=======
        usuario.clave = make_password("Password123")
        hash_original = usuario.clave
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
        mock_get.return_value = usuario

        result = autenticar_usuario(
            "juan@example.com",
            "incorrecta",
        )

        self.assertIsNone(result)
<<<<<<< HEAD
=======
        self.assertEqual(usuario.clave, hash_original)
        usuario.save.assert_not_called()

    @patch("apps.usuarios.services.Usuario.objects.get")
    def test_autenticar_usuario_inexistente(self, mock_get):
        from apps.usuarios.models import Usuario

        mock_get.side_effect = Usuario.DoesNotExist

        result = autenticar_usuario(
            "inexistente@example.com",
            "Password123",
        )

        self.assertIsNone(result)
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042

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

<<<<<<< HEAD
        mock_filter.assert_called_once_with(id_rol_fk=3)
=======
        mock_filter.assert_called_once_with(
            id_rol_fk=ROL_TECNICO
        )
>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
        queryset.order_by.assert_called_once_with("nombres")
        self.assertEqual(result, ["tecnico"])


class TestEquiposServices(SimpleTestCase):
<<<<<<< HEAD
=======

>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
    @patch("apps.equipos.services.Equipo.objects.select_related")
    def test_listar_equipos_ordena_por_codigo(self, mock_select_related):
        queryset = Mock()
        queryset.order_by.return_value = ["equipo1", "equipo2"]
        mock_select_related.return_value = queryset

        result = listar_equipos()

        mock_select_related.assert_called_once_with(
            "id_tipo_equipo_fk",
            "id_ubicacion_fk",
        )
        queryset.order_by.assert_called_once_with("codigo")
        self.assertEqual(result, ["equipo1", "equipo2"])


class TestSolicitudesServices(SimpleTestCase):
<<<<<<< HEAD
=======

>>>>>>> 035ab46f93a09b1663ac2b8f0c1ff71d737b9042
    @patch("apps.solicitudes.services.Solicitud.objects.filter")
    def test_contar_solicitudes_pendientes_incluye_las_asignadas(self, mock_filter):
        queryset = Mock()
        queryset.count.return_value = 4
        mock_filter.return_value = queryset

        result = contar_solicitudes_pendientes()

        mock_filter.assert_called_once_with(estado="pendiente")
        self.assertEqual(result, 4)
