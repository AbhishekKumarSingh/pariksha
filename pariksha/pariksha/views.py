from __future__ import absolute_import
from django.views import generic
from django.contrib.auth.models import User

from .forms import RegistrationForm
# create your views here

class SignupView(generic.CreateView):
    form_class = RegistrationForm
    model = User
    template_name = 'accounts/signup.html'
