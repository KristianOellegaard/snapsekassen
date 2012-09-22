from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from schnappsaccount.models import Person

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(queryset=Person.objects.all())),
)
