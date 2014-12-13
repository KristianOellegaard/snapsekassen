from django.conf.urls import *
from schnappsaccount.models import Person
from schnappsaccount.views import PersonListView
from schnappsaccount.api import ClaimResource, PersonResource
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(PersonResource())
v1_api.register(ClaimResource())

urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
    url(r'^$', PersonListView.as_view()),
)
