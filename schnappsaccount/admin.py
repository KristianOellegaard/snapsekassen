from django.contrib import admin
from models import Person, Claim

class ClaimAdmin(admin.ModelAdmin):
    list_display = ('person', 'reported_by', 'date')

admin.site.register(Person)
admin.site.register(Claim, ClaimAdmin)
