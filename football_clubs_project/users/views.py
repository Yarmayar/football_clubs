from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import LoginUserForm, RegisterUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Authentication'}


# def logout_user(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('users:login'))

def register(request):
    if request.POST:
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'users/register_done.html', {'title': 'Welcome!', 'name': user.username})
    else:
        form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form})
