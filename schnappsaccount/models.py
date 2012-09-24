from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return self.name

class Claim(models.Model):
    person = models.ForeignKey(Person)
    reason = models.TextField(blank=True)
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    reported_by = models.ForeignKey(Person, related_name='claim_report_set',
                                   blank=True, null=True)

    def __unicode__(self):
        return self.reason
