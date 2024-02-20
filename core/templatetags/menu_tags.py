from django import template
from core.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_items):
    return {'menu_items': menu_items, 'request': context['request']}
