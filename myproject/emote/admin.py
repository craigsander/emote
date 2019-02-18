from django.contrib import admin
from . import models



class IncidentAdmin(admin.ModelAdmin):
    model = models.Incident
    list_display = ['__all__', ]

admin.site.register(models.Incident, IncidentAdmin)


class CheckinAdmin(admin.ModelAdmin):
    model = models.Checkin
    list_display = ['__all__', ]

admin.site.register(models.Checkin, CheckinAdmin)

class QuoteAdmin(admin.ModelAdmin):
    model = models.Quote
    list_display = ['__all__', ]

admin.site.register(models.Quote, QuoteAdmin)
