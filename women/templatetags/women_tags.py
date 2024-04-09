from django import template
import women.views as views

register = template.Library()

@register.simple_tag()
def get_categories():
    return views.cats_db

@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected=None):
    cats = views.cats_db
    return {'cats': cats, 'cat_selected': cat_selected}

@register.inclusion_tag('women/menu_categories.html')
def show_menu(menu_selected=None):
    menu = views.menu
    return {'menu': menu, 'menu_selected': menu_selected}