from __future__ import unicode_literals

from django.db import models


class LightSample(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    state = models.BooleanField()
