from django.conf import settings
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
        MenuItem(_("Subscriptions"), view_name="account-subscription", icon="mfa"),
    ],
)

ActivityStreamMenu = Menu(
    _("Activity"),
    children=[
        MenuItem(
            _("Followers"),
            view_name="account-followers",
        ),
        MenuItem(
            _("Following"),
            view_name="account-following",
        ),
    ],
)

# This is the main menu for django-account-management which is displayed as a sidebar when editing user related
# information.
AccountMenu = Menu(
    "AccountMenu",
    root_template=getattr(settings, "DAC_MENU", "account_management/menu.html"),
    children=[
        AllAuthMenu,
        ActivityStreamMenu,
    ],
)

# This is the floating offcanvas menu which can be made available on any page
FloatingAccountMenu = Menu(
    "FloatingAccountMenu",
    root_template=getattr(settings, "DAC_FLOATING_MENU", "account_management/menu.html"),
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
