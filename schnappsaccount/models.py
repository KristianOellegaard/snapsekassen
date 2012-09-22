from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

class Claim(models.Model):
    person = models.ForeignKey(Person)
    reason = models.TextField(blank=True)
    debt = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return self.reason