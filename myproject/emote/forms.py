from django.forms import ModelForm
from .models import Checkin, Incident

	
class CheckinForm(ModelForm):
	class Meta:
		model = Checkin
		fields = ['feeling', 'intensity', 'location', 'details']
		
		
class IncidentForm(ModelForm):
	class Meta:
		model = Incident
		fields = ['incidentType', 'location', 'details']
