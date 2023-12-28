from django import template
from clubs import views
from clubs.models import Country, TagClub

register = template.Library()


@register.simple_tag()
def get_countries():
    return views.cntr_db


@register.inclusion_tag('clubs/list_countries.html')
def show_countries(cntr_selected):
    countries = Country.objects.all()
    return {'countries': countries, 'cntr_selected': cntr_selected}


@register.inclusion_tag('clubs/list_tags.html')
def show_all_tags():
    tags = TagClub.objects.all()
    return {'tags': tags}