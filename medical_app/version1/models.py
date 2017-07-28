from __future__ import unicode_literals
from django.db import models


class UserDetail(models.Model):

    email = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=10)
    name = models.CharField(max_length=35)
    contact_number = models.IntegerField()
    date_of_birth = models.DateTimeField()
    gender = models.CharField(max_length=1)

    created_on = models.DateTimeField(auto_now_add=True)
    last_updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.email)