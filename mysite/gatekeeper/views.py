from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Sugestion

def index(request):
	"""
	Renders the initial page
	"""
	return HttpResponse("Esse vai ser um app incrível")

def sugestions(request, sugestion_id):
	"""
	Renders a sugestion for a pitch.
	"""
	return HttpResponse("This is the sugestion number %s." % sugestion_id)

def add_sugestion(request):
	"""
	Create a form to add a sugestion.
	"""

	return render(request, 'gatekeeper/add_sugestion.html')
