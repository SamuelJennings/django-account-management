import flex_menu
from cotton_bs5.menus import SidebarGroup, SidebarItem
from django.conf import settings
from django.utils.translation import gettext_lazy as _

is_staff_user = lambda request: request.user.is_staff


# contains menu items for django-allauth
AllAuthMenu = SidebarGroup(
    _("Account"),
    children=[
        SidebarItem(
            _("Password"),
            view_name="account_change_password",
            icon="password_change",
        ),
        SidebarItem(_("Connected Accounts"), view_name="socialaccount_connections", icon="link"),
        SidebarItem(_("Emails"), view_name="account_email", icon="email"),
        SidebarItem(_("Sessions"), view_name="usersessions_list", icon="sessions"),
        SidebarItem(_("MFA"), view_name="mfa_index", icon="mfa"),
        SidebarItem(_("Subscriptions"), view_name="account-subscription", icon="mfa"),
    ],
)

ActivityStreamMenu = SidebarGroup(
    _("Activity"),
    children=[
        SidebarItem(_("Recent Activity"), view_name="home", icon="activity"),
        SidebarItem(_("Following"), view_name="account-following", icon="star-solid"),
        SidebarItem(_("Followed by"), view_name="account-followers", icon="identifier"),
    ],
)

# This is the main menu for django-account-management which is displayed as a sidebar when editing user related
# information.
AccountMenu = flex_menu.Menu(
    "AccountMenu",
    root_template="fairdm/menus/detail.html",
    children=[
        AllAuthMenu,
        ActivityStreamMenu,
    ],
)

# This is the floating offcanvas menu which can be made available on any page
FloatingAccountMenu = flex_menu.Menu(
    "FloatingAccountMenu",
    root_template=getattr(settings, "DAC_FLOATING_MENU", "account_management/menu.html"),
    label=_("Account"),
    children=[
        AllAuthMenu.copy(),
    ],
)


# Groups all django-account-management menus under a single menu
AccountManagement = flex_menu.Menu(
    "Account Management",
    children=[AccountMenu, FloatingAccountMenu],
)
