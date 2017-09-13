from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import RegistrationForm
from .models import Profile

class IndexView(View):
	template_name = 'accounts/index.html'

class RegisterView(View):
	form_class = RegistrationForm
	template_name = 'accounts/register.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit = False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			# return User objects if credentials are correct
			user = authenticate(username=username, password=password)
			if user is not None:

				if user.is_active:
					login(request, user)
					return redirect('accounts:profile-create')

		# if login fails
		return render(request, self.template_name, {'form': form})

# class ProfileCreate(CreateView):
# 	model = Profile
# 	fields = ['fullname', 'gender', 'birth_date', 'contact', 'organization', 'photo']
# 	template_name = 'accounts/create_profile.html'
#
# class ProfileView(generic.ListView):
# 	model = Profile
# 	template_name= 'accounts/profile.html'
