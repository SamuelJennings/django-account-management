from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
    path("", TemplateView.as_view(template_name="account_management/base.html"), name="home"),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]

