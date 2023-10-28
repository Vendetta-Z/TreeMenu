from django import template
from TreeMenu.models import MenuItem
register = template.Library()   


@register.inclusion_tag('menu.html', takes_context=True)
def show_menu(context, name):
    menu_items = MenuItem.objects.filter(level=1)
    return {
        "menu_items": menu_items,
        "menu_name": name
    }