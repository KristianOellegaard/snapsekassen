from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import DjangoAuthorization, ReadOnlyAuthorization
from tastypie.authentication import BasicAuthentication
from schnappsaccount.models import Claim,Person
from django.contrib.auth.models import User

class AnonymousGetAuthentication(BasicAuthentication):
    def is_authenticated(self,request,**kwargs):
        if request.method == "GET":
            return True
        else:
            return super(BasicAuthentication, self).is_authenticated(request, **kwargs)

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all();
        resource_name = 'user'
        fields = ['first_name', 'last_name', 'username']
        authorization = ReadOnlyAuthorization()

class PersonResource(ModelResource):
    class Meta:
        queryset = Person.objects.all()
        resource_name = 'person'
        authorization = ReadOnlyAuthorization()

class ClaimResource(ModelResource):
    person = fields.ForeignKey(PersonResource, 'person')
    reported_by = fields.ForeignKey(PersonResource, 'reported_by')
    class Meta:
        queryset = Claim.objects.all()
        resource_name = 'claim'
        authentication = AnonymousGetAuthentication()
        authorization = DjangoAuthorization()
