from django.forms import ModelForm, HiddenInput
from .models import Checkin, Incident

	
class CheckinForm(ModelForm):
	class Meta:
		model = Checkin
		fields = ['person', 'feeling', 'intensity', 'location', 'details']
		widgets = {'person': HiddenInput()}
		
class IncidentForm(ModelForm):
	class Meta:
		model = Incident
		fields = ['incidentType', 'location', 'details']
