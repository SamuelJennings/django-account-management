import logging

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from flex_menu import Menu, MenuItem

logger = logging.getLogger(__name__)

is_staff_user = lambda request: request.user.is_staff


# Example Usage:
MainMenu = Menu(
    "MainMenu",
    children=[
        Menu(
            _("Account"),
            children=[
                MenuItem(
                    _("password"),
                    view_name="account_change_password",
                    icon="password_change",
                ),
                MenuItem(
                    _("Connected Accounts"),
                    view_name="socialaccount_connections",
                    icon="link",
                ),
                MenuItem(
                    _("emails"),
                    view_name="account_email",
                    icon="email",
                ),
                MenuItem(
                    _("Sessions"),
                    view_name="usersessions_list",
                    icon="sessions",
                ),
                MenuItem(_("MFA"), view_name="mfa_index", icon="mfa"),
            ],
        ),
    ],
)


AccountMenu = Menu(
    "AccountMenu",
    label=_("Account"),
    children=[
        MenuItem(
            _("password"),
            view_name="account_change_password",
            icon="password_change",
        ),
        MenuItem(
            _("Connected Accounts"),
            view_name="socialaccount_connections",
            icon="link",
        ),
        MenuItem(_("emails"), view_name="account_email", icon="email"),
        MenuItem(_("Sessions"), view_name="usersessions_list", icon="sessions"),
        MenuItem(_("MFA"), view_name="mfa_index", icon="mfa"),
    ],
)


def get_profile_url(request):
    return reverse_lazy("profile-edit", kwargs={"pk": request.user.pk})


# ProfileMenu = Menu(
#     "ProfileMenu",
#     label=_("Profile"),
#     children=[
#         MenuItem(_("Profile"), url=get_profile_url, icon="user"),
#     ],
# )

UserManagementMenu = Menu(
    "Account Management",
    children=[
        # ProfileMenu,
        AccountMenu,
    ],
)
