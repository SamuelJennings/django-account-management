from django.urls import path

# from debug_toolbar import urls as debug_toolbar
from .views import Home

urlpatterns = [
    path("", Home.as_view(), name="account-management"),
]
