# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

EXTRAVERSION_OPTION = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)
# Reservado/Carismático
NEUROTICISM_OPTION = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)
# Nervoso/Confiante
AGREEABLENESS_OPTION = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)
# Não-amigável/Amigável


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Participant(models.Model):
    participant_name = models.CharField(max_length=200)
    participant_age = models.IntegerField()


class Questionnaire(models.Model):

    extraversion = models.CharField(
        max_length=1, choices=EXTRAVERSION_OPTION, default='1')
    neuroticism = models.CharField(
        max_length=1, choices=NEUROTICISM_OPTION, default='1')
    agreeableness = models.CharField(
        max_length=1, choices=AGREEABLENESS_OPTION, default='1')

# Create your models here.
