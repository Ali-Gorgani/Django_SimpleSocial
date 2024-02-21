from django.shortcuts import render
from accounts.models import User
from django.urls import reverse_lazy
from accounts.forms import SignUpForm
from django.views.generic import CreateView


# Create your views here.
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'
