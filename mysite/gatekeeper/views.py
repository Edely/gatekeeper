from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import SugestionForm
from django.utils import timezone


from .models import Sugestion

def index(request):
	"""
	Renders the initial page
	"""
	all_sugestions = Sugestion.objects.all()

	return render(request,'gatekeeper/index.html', {'all_sugestions': all_sugestions} )

def sugestions(request, sugestion_id):
	"""
	Renders a sugestion for a pitch.
	"""
	sugestion = Sugestion.objects.get(pk=sugestion_id)
	return render(request, 'gatekeeper/sugestion_detail.html', { 'sugestion': sugestion })

def add_sugestion(request):
	"""
	Create a form to add a sugestion.
	"""
	if request.method == 'POST':
		form = SugestionForm(request.POST)

		if form.is_valid():
			sugestion = form.save(commit=False)
			sugestion.pub_date = timezone.now()
			sugestion.save()

			return HttpResponseRedirect(reverse('gatekeeper:index'))

	else:
		form = SugestionForm()


	return render(request, 'gatekeeper/add_sugestion.html', {'form':form})
