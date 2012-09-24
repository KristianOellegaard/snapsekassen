from django.views.generic import ListView
from models import Claim
from django.db.models import Sum


class PersonListView(ListView):
    def get_context_data(self):
        total_sum = Claim.objects.aggregate(Sum('debt'))
        return {'total_sum': total_sum}
