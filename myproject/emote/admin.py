from django.contrib import admin
from . import models



class IncidentAdmin(admin.ModelAdmin):
    model = Incident
    list_display = ['__all__', ]

admin.site.register(Incident, IncidentAdmin)


class CheckinAdmin(admin.ModelAdmin):
    model = Checkin
    list_display = ['__all__', ]

admin.site.register(Checkin, CheckinAdmin)

class QuoteAdmin(admin.ModelAdmin):
    model = Quote
    list_display = ['__all__', ]

admin.site.register(Quote, QuoteAdmin)
