from __future__ import absolute_import
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User

from .forms import RegistrationForm
# create your views here

class HomePageView(generic.TemplateView):
    template_name = 'home.html'

class SignupView(generic.CreateView):
    form_class = RegistrationForm
    model = User
    success_url = reverse_lazy('home')
    template_name = 'accounts/signup.html'
