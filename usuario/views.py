# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, RedirectView, CreateView, UpdateView, ListView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import forms, login, logout, authenticate
from django.views.generic import View
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm


class LoginView(FormView):
    template_name = 'usuario/login.html'
    form_class = LoginForm

    def get_success_url(self):
        return reverse_lazy('post_lista')

    def form_valid(self, form):
        usuario = form.cleaned_data['username']
        contrasena = form.cleaned_data['password']
        usuario = authenticate(username=usuario, password=contrasena)
        login(self.request, usuario)
        return super(LoginView, self).form_valid(form)


class RegisterUser(CreateView):
    model = User
    template_name = "usuario/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('login')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')