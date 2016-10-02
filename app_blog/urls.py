#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
#from .views import IndexTemplate



urlpatterns = [
    url(r'^$', views.PostLista.as_view(), name='post_lista'),
  	url(r'^nuevo$', views.PostCrear.as_view(), name='post_nuevo'),
  	url(r'^editar/(?P<pk>\d+)$', views.PostActualizar.as_view(), name='post_editar'),
  	url(r'^eliminar/(?P<pk>\d+)$', views.PostEliminar.as_view(), name='post_eliminar'),
]