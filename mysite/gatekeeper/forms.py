from django import forms
from .models import Sugestion

class SugestionForm(forms.ModelForm):
	"""
	Creates the form to add a sugestion.
	"""

	class Meta:
		model = Sugestion
		fields = {'title', 'description'}
		widgets = {
			'description': forms.Textarea(attrs={'class': 'materialize-textarea'})
		}
