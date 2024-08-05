
from django.utils.translation import gettext_lazy as _
from simple_menu import Menu
import logging
from contextlib import suppress

from django.urls import reverse, reverse_lazy
from django.urls.exceptions import NoReverseMatch
from django.utils.translation import gettext_lazy as _
import logging
from contextlib import suppress

from django.urls import reverse, reverse_lazy
from django.urls.exceptions import NoReverseMatch
from django.utils.translation import gettext_lazy as _
from simple_menu import MenuItem as SimpleMenuItem

logger = logging.getLogger(__name__)


def is_staff_user(request):
    return request.user.is_staff


def check_url(viewname):
    """Check to see if a url can be resolved. Return false if not."""

    def inner(request):
        with suppress(NoReverseMatch):
            return reverse(viewname)

    return inner

class MenuItem(SimpleMenuItem):

    def __init__(self, title, view_name="", url=None, children=[], weight=1, check=None,
                 visible=True, slug=None, exact_url=False, **kwargs):

        if not url and not view_name:
            raise ValueError("Either a URL or view_name must be provided")
        
        if view_name:
            with suppress(NoReverseMatch):
                url = reverse(view_name)
                check = lambda : False

        super().__init__(title, url, children, weight, check, visible, slug, exact_url, **kwargs)

    def check(self, request):
        try:
            reverse_lazy(self.url)
        except NoReverseMatch:
            logger.warning(f"Menu item {self.title} has an invalid URL: {self.url}")
            self.visible = False

        super().check(request)


class SubMenu(SimpleMenuItem):
    is_submenu = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, url=None, **kwargs)


class BaseMenu(dict):
    menu_name = ""
    submenus = {}

    @classmethod
    def add_item(c, item):
        """
        add_item adds MenuItems to the menu identified by 'name'
        """
        Menu.add_item(c.menu_name, item)

    @classmethod
    def add_items(c, *args):
        """
        add_item adds MenuItems to the menu identified by 'name'
        """
        for menu_item in args:
            if isinstance(menu_item, SubMenu):
                c.submenus[menu_item.title] = menu_item

            if isinstance(menu_item, MenuItem | SubMenu):
                c.add_item(menu_item)
            else:
                raise TypeError(f"add_items expected a MenuItem, but got {type(menu_item)}")
            
class MenuItem(SimpleMenuItem):

    def __init__(self, title, view_name="", url=None, children=[], weight=1, check=None,
                 visible=True, slug=None, exact_url=False, **kwargs):

        if not url and not view_name:
            raise ValueError("Either a URL or view_name must be provided")
        

        if view_name:
            visible = False
            with suppress(NoReverseMatch):
                url = reverse(view_name)
                visible = True
                # check = lambda : False

        super().__init__(title, url, children, weight, check, visible, slug, exact_url, **kwargs)

    def check(self, request):
        try:
            reverse_lazy(self.url)
        except NoReverseMatch:
            logger.warning(f"Menu item {self.title} has an invalid URL: {self.url}")
            self.visible = False

        super().check(request)