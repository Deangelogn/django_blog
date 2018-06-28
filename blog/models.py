# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


STATUS_CHOICES = (
    (1, ("Not relevant")),
    (2, ("Review")),
    (3, ("Maybe relevant")),
    (4, ("Relevant")),
    (5, ("Leading candidate"))
)


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
    extrovertion = models.IntegerField(choices=STATUS_CHOICES, default=1)

# Create your models here.
