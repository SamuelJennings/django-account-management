from django.urls import path

from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="account-management"),
    path("account/followers/", views.AccountFollowers.as_view(), name="account-followers"),
    path("account/following/", views.AccountFollowing.as_view(), name="account-following"),
    path("entrance/", views.EntranceView.as_view(), name="account-entrance"),
]
