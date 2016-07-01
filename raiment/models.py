from __future__ import unicode_literals
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200, null=True)
    text = models.TextField(null=True)
    image = models.ImageField(null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
