from django.shortcuts import redirect
from django.views.generic import TemplateView


class AuthenticatedPageView(TemplateView):

    def dispatch(self, request, *args, **kwargs):
        usuario_id = request.session.get("usuario_id")

        if not usuario_id:
            return redirect("login")

        return super().dispatch(
            request,
            *args,
            **kwargs,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["usuario_id"] = self.request.session.get(
            "usuario_id"
        )

        context["usuario_nombre"] = self.request.session.get(
            "usuario_nombre"
        )

        context["usuario_email"] = self.request.session.get(
            "usuario_email"
        )

        return context


class InicioPageView(AuthenticatedPageView):
    template_name = "index.html"


class HistorialPageView(AuthenticatedPageView):
    template_name = "historial.html"


class PerfilPageView(AuthenticatedPageView):
    template_name = "perfil.html"


class TecnicoPageView(AuthenticatedPageView):
    template_name = "tecnico.html"


class PerfilTecnicoPageView(AuthenticatedPageView):
    template_name = "perfil_tecnico.html"


class AdminHomePageView(AuthenticatedPageView):
    template_name = "admin_home.html"


class ReportesRecientesPageView(AuthenticatedPageView):
    template_name = "reportes_recientes.html"


class TecnicosAdminPageView(AuthenticatedPageView):
    template_name = "tecnicos_admin.html"


class HistorialAdminPageView(AuthenticatedPageView):
    template_name = "historial_admin.html"


class EquiposAdminPageView(AuthenticatedPageView):
    template_name = "equipos_admin.html"


class AsignacionesPageView(AuthenticatedPageView):
    template_name = "asignaciones.html"


class EquiposPageView(AuthenticatedPageView):
    template_name = "equipos.html"


class PiezasPageView(AuthenticatedPageView):
    template_name = "piezas.html"


class SolicitudesPageView(AuthenticatedPageView):
    template_name = "solicitudes.html"


class MantenimientosPageView(AuthenticatedPageView):
    template_name = "mantenimientos.html"


class ReportesPageView(AuthenticatedPageView):
    template_name = "reportes.html"