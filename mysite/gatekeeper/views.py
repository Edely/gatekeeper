from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Esse vai ser um app incrível")

def SugestionView():
	pass