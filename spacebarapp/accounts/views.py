from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView
# Create your views here.
from . import forms


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse('Login')
    template_name = 'accounts/signup.html'
