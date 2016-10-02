#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.shortcuts import render
from .models import *



class IndexTemplate(TemplateView):
	template_name = "app_blog/index.html"