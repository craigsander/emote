from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from .forms import IncidentForm, CheckinForm
from . import models


def links(request, template_name='index.html'):

	return render_to_response(template_name, locals())
	

def checkin(request, template_name='checkin.html'):
	
	if request.method == 'POST':
		f = CheckinForm(request.POST)
		if f.is_valid():
			f.save()
			return HttpResponseRedirect('/thanks/')
		else:
			f = CheckinForm()
	else:
		f=CheckinForm()
	
	return render_to_response(template_name, locals())
	

def incident(request, template_name='incident.html'):
	
	if request.method == 'POST':
		f = IncidentForm(request.POST)
		if f.is_valid():
			f.save()
			return HttpResponseRedirect('/thanks-incident/')
		else:
			f = IncidentForm()
	else:
		f = IncidentForm()
	
	return render_to_response(template_name, locals())
