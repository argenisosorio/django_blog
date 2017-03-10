#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from app_blog.models import Post
from django.forms import (
    TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput
)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post

        fields = [
            'autor',
            'titulo',
            'cuerpo',
        ]

        widgets = {
            'autor': forms.TextInput(attrs={
                'class':'form-control input-md',
                'style': 'min-width: 0; width: 50%; display: inline;',
            }),
            'titulo': forms.TextInput(attrs={
                'class':'form-control input-md',
                'style': 'min-width: 0; width: 50%; display: inline;',
            }),
            'cuerpo': forms.Textarea(attrs={
                'class':'form-control input-md',
                'style': 'min-width: 0; width: 50%; display: inline;',
            }),
        }