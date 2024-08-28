from django.views.generic import TemplateView

from account_management.menus import MainMenu


class Home(TemplateView):
    template_name = "account_management/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = MainMenu
        return context
