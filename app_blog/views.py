#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.shortcuts import render
from .models import *
from django.contrib.messages.views import SuccessMessageMixin


class PostLista(ListView):
    model = Post


class PostCrear(SuccessMessageMixin,CreateView):
    model = Post
    fields = ['autor', 'titulo', 'cuerpo', 'fecha']
    success_url = reverse_lazy('post_lista')
    success_message = "Se creó la publicación con éxito"


class PostActualizar(SuccessMessageMixin,UpdateView):
    model = Post
    fields = ['autor', 'titulo', 'cuerpo', 'fecha']
    success_url = reverse_lazy('post_lista')
    success_message = "Se actualizó la publicación con éxito"


class PostEliminar(SuccessMessageMixin,DeleteView):
    model = Post
    fields = ['autor', 'titulo', 'cuerpo', 'fecha']
    success_url = reverse_lazy('post_lista')
    success_message = "Se eliminó la publicación con éxito"