from django import forms
from .models import Sugestion, Citizen, User

class SugestionForm(forms.ModelForm):
	"""
	Creates the form to add a sugestion.
	"""

	class Meta:
		model = Sugestion
		fields = {'title', 'description'}
		widgets = {
			'description': forms.Textarea(attrs={'class': 'materialize-textarea validate'}),
			'title': forms.TextInput(attrs={'class': 'validate'})
		}

class SigninForm(forms.ModelForm):
	"""
	Cerates the form to sign in for the first time.
	"""
	class Meta:
		model = Citizen
		fields = {'neighbourhood', 'username', 'password', 'email', 'first_name', 'last_name'}
		widgets = {
			'neighbourhood': forms.Textarea(attrs={'class': 'validate'}),
			'username': forms.TextInput(attrs={'class': 'validate'})
		}