from django.urls import path, register_converter

from . import views, converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.ClubsHome.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('addclub/', views.AddClub.as_view(), name='add_club'),
    path('feedback/', views.feedback, name='feedback'),
    path('login/', views.login, name='login'),
    path('club/<slug:club_slug>', views.ShowClub.as_view(), name='club'),
    path('country/<slug:country_slug>/', views.ClubsCountry.as_view(), name='country'),
    path('tag/<slug:tag_slug>/', views.ClubsTag.as_view(), name='tag'),
]