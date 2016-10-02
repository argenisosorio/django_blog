#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from .views import IndexTemplate



urlpatterns = [
    url(r'^$', IndexTemplate.as_view(), name='index'),
]