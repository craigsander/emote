from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect


def links(request, template_name='index.html'):

	return render_to_response(template_name, locals())
	

def checkin(request, template_name='test.html'):
	
	return render_to_response(template_name, locals())
	

def incident(request, template_name='test.html'):
	
	return render_to_response(template_name, locals())
