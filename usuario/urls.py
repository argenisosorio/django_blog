# -*- coding: utf-8 -*-
from django.conf.urls import url
from usuario import views
from usuario.views import *
import usuario.views as views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', LoginView.as_view(), name = "login"),
    url(r'^register', RegisterUser.as_view(), name="register"),
    url(r'logout/$', views.Logout.as_view(), name='logout'),
]