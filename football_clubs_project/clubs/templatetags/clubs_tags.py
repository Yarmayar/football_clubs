from django import template
from clubs import views

register = template.Library()


@register.simple_tag()
def get_countries():
    return views.cntr_db


@register.inclusion_tag('clubs/list_countries.html')
def show_countries(cntr_selected):
    return {'countries': views.cntr_db, 'cntr_selected': cntr_selected}
