# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Participant, Input

admin.site.register(Post)
admin.site.register(Participant)
admin.site.register(Input)

# Register your models here.
