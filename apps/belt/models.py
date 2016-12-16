from __future__ import unicode_literals
from ..first_app.models import User
from django.db import models

# Create your models here.
class Poke(models.Model):
    one_poking = models.ForeignKey('first_app.User', null=True, related_name = "poker")
    one_getting_poked = models.ForeignKey('first_app.User', null=True, related_name= "pokee")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
