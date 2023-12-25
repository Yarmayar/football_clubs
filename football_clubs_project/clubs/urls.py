from django.urls import path, register_converter

from . import views, converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index),
    path('countries/<int:cntr_id>/', views.countries),
    path('countries/<slug:cntr_slug>/', views.countries_by_slug),
    path('archive/<year4:year>/', views.archive),
]