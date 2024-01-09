from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordChangeDoneView

from users import views

app_name = 'users'


urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
    path('password_change/', views.ChangePassword.as_view(title='Changing password'), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html',
                                                                       title='New password created'),
         name='password_change_done'),
]