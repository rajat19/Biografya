import re
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget
from django.core.exceptions import ObjectDoesNotExist
from django import forms

class RegistrationForm(forms.ModelForm):
	username = forms.CharField(label='Username', max_length=30)
	email = forms.CharField(label='Email', max_length=50)
	password = forms.CharField(widget = forms.PasswordInput)
	confirm_password = forms.CharField(widget = forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password', 'confirm_password']

	def clean_confirm_password(self):
		if 'password' in self.cleaned_data:
			password = self.cleaned_data['password']
			confirm_password = self.cleaned_data['confirm_password']
		if password == confirm_password:
			return confirm_password
		raise forms.ValidationError('Passwords do not match.')

	def clean_username(self):
		username = self.cleaned_data['username']
		if not re.search(r'^\w+$', username):
			raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
		try:
			User.objects.get(username=username)
		except ObjectDoesNotExist:
			return username
		raise forms.ValidationError('Username is already taken.')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			User.objects.get(email=email)
		except ObjectDoesNotExist:
			return email
		raise forms.ValidationError('Email already exists')
