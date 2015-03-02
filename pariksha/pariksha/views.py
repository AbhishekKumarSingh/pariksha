from __future__ import absolute_import
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import RegistrationForm, LoginForm
# create your views here

class HomePageView(generic.TemplateView):
    template_name = 'home.html'

class SignupView(generic.CreateView):
    form_class = RegistrationForm
    model = User
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        ret = super(SignupView, self).form_valid(form)
        messages.success(self.request, "Thanks for registering, go ahead and "
                                       "login")
        return ret


class LoginView(generic.FormView):
    form_class = LoginForm
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
