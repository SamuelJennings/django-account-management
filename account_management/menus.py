import logging

from django.utils.translation import gettext_lazy as _

from .utils import BaseMenu, MenuItem, SubMenu

logger = logging.getLogger(__name__)


is_staff_user = lambda request: request.user.is_staff


class AccountOffCanvas(BaseMenu):
    menu_name = "account_offcanvas"

class AccountSidebar(BaseMenu):
    menu_name = "account_sidebar"


AccountSidebar.add_items(
    SubMenu(
        _("General"),
        weight=2,
        children=[
            MenuItem(_("appearance"), view_name="user:appearance-settings", icon="fas fa-paintbrush"),
            # MenuItem(_("notifications"), view_name="user:notifications-settings"), icon="fas fa-bell"),
            # MenuItem(_("privacy"), view_name="contributor-profile"), icon="fas fa-user-secret"),
        ],
    ),
    SubMenu(
        _("Account"),
        weight=3,
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
                _("API Tokens"),
                view_name="api-tokens",
                icon="key",
            ),
            MenuItem(
                _("Sessions"),
                view_name="usersessions_list",
                icon="sessions",
            ),
            MenuItem(_("MFA"), view_name="mfa_index", icon="mfa"),
        ],
    ),
    # SubMenu(
    #     _("Agreements"),
    #     weight=4,
    #     children=[
    #         MenuItem(_("Code of Conduct"), url=view_name="user:code_of_conduct"), icon="fas fa-file-contract"),
    #         # MenuItem(_("Terms of Use"), url=view_name="user:terms"), icon="fas fa-file-contract"),
    #     ],
    # ),
)


AccountOffCanvas.add_items(
    # MenuItem(_("Manage Profile"), view_name="contributor-profile", icon=icon("person")),
    # MenuItem(_("Recent Activity"), view_name="contributor-profile", icon="fas fa-rss"),
    # MenuItem(_("Following"), view_name="contributor-profile", icon="fas fa-star"),
    MenuItem(_("Site administration"), view_name="admin:index", check=is_staff_user, icon="site_admin"),
    SubMenu(
        _("Account"),
        # weight=20,
        children=[
            MenuItem(_("Emails"), view_name="account_email", icon="email"),
            MenuItem(_("Connected Accounts"), view_name="socialaccount_connections", icon="link"),
        ],
    ),
    MenuItem(_("Logout"), view_name="account_logout", icon="logout", extra_classes="position-absolute bottom-0 start-0 bg-danger text-center text-light", htmx={"hx-method": "POST", "hx-vals": "logout", }),
)
