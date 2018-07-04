# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Participant, Questionnaire

admin.site.register(Post)
admin.site.register(Participant)
admin.site.register(Questionnaire)

# Register your models here.
