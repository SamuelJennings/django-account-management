from django import template
from django.conf import settings
from django.utils.module_loading import import_string

register = template.Library()


@register.simple_tag
def avatar_url(user, **kwargs):
    """Renders a default img tag for the given profile. If the profile.image is None, renders a default icon if no image is set."""

    avatar_getter = getattr(settings, "ACCOUNT_MANAGEMENT_GET_AVATAR_URL", None)

    if avatar_getter is None:
        return None

    # avatar_getter should be a string specifiying a dotted path to a callable
    # the callable should accept a user and return an valid URL
    getter_func = import_string(avatar_getter)

    if callable(getter_func):
        return getter_func(user)
    else:
        return None
