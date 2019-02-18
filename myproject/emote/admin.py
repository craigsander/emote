from django.contrib import admin
from . import models



class IncidentAdmin(admin.ModelAdmin):
    model = models.Incident
    list_display = ['created', 'incidentType', 'location']

admin.site.register(models.Incident, IncidentAdmin)


class CheckinAdmin(admin.ModelAdmin):
    model = models.Checkin
    list_display = ['created', 'feeling', 'intensity', 'location' ]

admin.site.register(models.Checkin, CheckinAdmin)

class QuoteAdmin(admin.ModelAdmin):
    model = models.Quote
    list_display = ['id', ]

admin.site.register(models.Quote, QuoteAdmin)
