from django.views.generic import ListView
from models import Claim, Person
from django.db.models import Sum


class PersonListView(ListView):	
	model = Person
	def get_context_data(self, *args, **kwargs):
		context = super(PersonListView, self).get_context_data(**kwargs)
		context['object_list'] = Person.objects.all()
		context['total_sum'] = Claim.objects.aggregate(Sum('debt'))
		
		return context
