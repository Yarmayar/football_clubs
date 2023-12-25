from django.urls import path, register_converter

from . import views, converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('countries/<int:cntr_id>/', views.countries, name='cntr_id'),
    path('countries/<slug:cntr_slug>/', views.countries_by_slug, name='countries'),
    path('archive/<year4:year>/', views.archive, name='archive'),
]