from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from account_management.menus import AccountMenu


class Home(LoginRequiredMixin, TemplateView):
    template_name = "account_management/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = AccountMenu
        return context
