from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from .forms import IncidentForm, CheckinForm
from . import models

def get_random_item(max_id=None):
    if max_id is None:
        max_id = models.Quote.objects.aggregate(Max('id')).values()[0]
    min_id = math.ceil(max_id*random.random())
    return models.Quote.objects.filter(id__gte=min_id)[0]


def links(request, template_name='index.html'):

	return render_to_response(template_name, locals())
	

def checkin(request, template_name='checkin.html'):
	f=CheckinForm()
	
	if request.method == 'POST':
		f = CheckinForm(request.POST)
		if f.is_valid():
			f.save()
			return HttpResponseRedirect('/thanks/')
		else:
			f = CheckinForm()
	else:
		f=CheckinForm()
	
	return render(request, template_name, locals())
	

def incident(request, template_name='incident.html'):
	
	if request.method == 'POST':
		f = IncidentForm(request.POST)
		if f.is_valid():
			f.save()
			return HttpResponseRedirect('/thanks/')
		else:
			f = IncidentForm()
	else:
		f = IncidentForm()
	
	return render(request, template_name, locals())
	

def thanks(request, template_name='thanks.html'):
	
	return render(request, template_name, locals())
