from __future__ import absolute_import
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout

from .forms import RegistrationForm, LoginForm
from braces import views
# create your views here

class HomePageView(generic.TemplateView):
    template_name = 'home.html'

class SignupView(
    views.AnonymousRequiredMixin,
    views.FormValidMessageMixin,
    generic.CreateView
):
    form_class = RegistrationForm
    from_valid_message = 'Thanks for registering, go ahead and login'
    model = User
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class LoginView(
    views.AnonymousRequiredMixin,
    views.FormValidMessageMixin,
    generic.FormView
):
    form_class = LoginForm
    form_valid_message = "You're logged in now"
    success_url = reverse_lazy('home')
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class LogoutView(
    views.LoginRequiredMixin,
    views.MessageMixin,
    generic.RedirectView,
):
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        logout(self.request)
        self.messages.success(self.request, "You're logged out, come back soon")
        return super(LogoutView, self).get(self.request, *args, **kwargs)
