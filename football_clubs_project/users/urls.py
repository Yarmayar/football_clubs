from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView

from users import views

app_name = 'users'


urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
    path('password-change/', views.ChangePassword.as_view(title='Changing password'), name='password_change'),
    path('password-change/done/', views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html',
                                                                       title='New password created'),
         name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset_form.html',
                                                      email_template_name='users/password_reset_email.html',
                                                      success_url=reverse_lazy('users:password_reset_done'),
                                                      title='Reset password'),
                                                      name='password_reset'),
    path('password-reset/done/', PasswordResetView.as_view(
        template_name='users/password_reset_done.html',
        title='Reset password'),
        name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html',
        success_url=reverse_lazy('users:password_reset_complete'),
        title='Create new password'),
        name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html',
        title="New password's created"),
        name='password_reset_complete'),

]
