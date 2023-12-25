from django.urls import path, register_converter

from . import views, converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addclub/', views.add_club, name='add_club'),
    path('feedback/', views.feedback, name='feedback'),
    path('login/', views.login, name='login'),
    path('club/<int:club_id>', views.show_club, name='club'),
]