#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^lista$', login_required(views.PostLista.as_view()), name='post_lista'),
    url(r'^nuevo$', login_required(views.PostCrear.as_view()), name='post_nuevo'),
    url(r'^editar/(?P<pk>\d+)$', login_required(views.PostActualizar.as_view()), name='post_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(views.PostEliminar.as_view()), name='post_eliminar'),
    url(r'^detalle/(?P<pk>\d+)$', login_required(views.PostDetalle), name='post_detalle'),
]