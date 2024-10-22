from django.utils.translation import gettext_lazy as _
from flex_menu import Menu, MenuItem

is_staff_user = lambda request: request.user.is_staff

# contains menu items for django-allauth
AllAuthMenu = Menu(
    _("Account"),
    children=[
        MenuItem(
            _("Password"),
            view_name="account_change_password",
            icon="password_change",
        ),
        MenuItem(_("Connected Accounts"), view_name="socialaccount_connections", icon="link"),
        MenuItem(_("Emails"), view_name="account_email", icon="email"),
        MenuItem(_("Sessions"), view_name="usersessions_list", icon="sessions"),
        MenuItem(_("MFA"), view_name="mfa_index", icon="mfa"),
    ],
)

# This is the main menu for django-account-management which is displayed as a sidebar when editing user related
# information.
AccountMenu = Menu(
    "AccountMenu",
    children=[
        AllAuthMenu,
    ],
)

# This is the floating offcanvas menu which can be made available on any page
FloatingAccountMenu = Menu(
    "FloatingAccountMenu",
    label=_("Account"),
    children=[
        AllAuthMenu.copy(),
    ],
)


# Groups all django-account-management menus under a single menu
AccountManagement = Menu(
    "Account Management",
    children=[AccountMenu, FloatingAccountMenu],
)
