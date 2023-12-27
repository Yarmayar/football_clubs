from django.urls import path, register_converter

from . import views, converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addclub/', views.add_club, name='add_club'),
    path('feedback/', views.feedback, name='feedback'),
    path('login/', views.login, name='login'),
    path('club/<slug:club_slug>', views.show_club, name='club'),
    path('country/<int:cntr_id>/', views.show_country, name='country')
]