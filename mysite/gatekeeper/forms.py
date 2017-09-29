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
		fields = {'neighbourhood', 'username', 'email', 'first_name', 'last_name'}
		widgets = {
			'neighbourhood': forms.TextInput(attrs={'class': 'validate'}),
			'name': forms.TextInput(attrs={'class': 'validate'}),
			'first_name': forms.TextInput(attrs={'class': 'validate'}),
			'last_name': forms.TextInput(attrs={'class': 'validate'}),
			'email_name': forms.EmailInput(attrs={'class': 'validate'}),
			'password': forms.PasswordInput(attrs={'class': 'validate'}),
		}