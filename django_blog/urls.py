# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('usuario.urls')),
	url(r'^', include('app_blog.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^captcha/', include('captcha.urls'))
]
