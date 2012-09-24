from django.conf.urls import patterns, url
from schnappsaccount.models import Person
from schnappsaccount.views import PersonListView

urlpatterns = patterns('',
    url(r'^$', PersonListView.as_view()),
)
