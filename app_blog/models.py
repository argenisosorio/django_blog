#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime



class Post(models.Model):
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    cuerpo = models.TextField(max_length=200)
    fecha = models.DateField(default=datetime.now, help_text='')

    def __unicode__(self):
        return self.autor

	def get_absolute_url(self):
		return reverse('post_editar', kwargs={'pk': self.pk})