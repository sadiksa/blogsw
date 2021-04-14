from django.shortcuts import render
from django.views import generic
from .forms import SignUpForm
from django.urls import reverse_lazy
# Create your views here.


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

#  i did not use login view. But thanks to urls auth.urls area default django lgin page works for us.
