from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.timezone import utc
from django.views.generic import View
from .models import Details, Education, Experience, Project

class IndexView(ListView):
    pass

@method_decorator(login_required, name="dispatch")
class ProfileCreate(CreateView):
    form_class = ProfileForm
    template_name = 'resume/profile_create.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            profile = form.save(commit = False)
            profile.user = request.user
            # fname, extension = os.splitext(form.cleaned_data['photo'].name)
            profile.save()

        else:
            return render(request, self.template_name, {'errors': form.errors})

        return redirect('resume:index')

class ProfileUpdate(generic.DetailView):
    model = Details
    template_name = 'resume/profile_update.html'
    fields = ['first_name', 'last_name', 'birth_date', 'gender', 'contact', 'address', 'facebook', 'github', 'linkedin']

class ExperienceAdd(generic.DetailView):
    form_class = ExperienceForm
    template_name = 'resume/experience_add.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            profile = form.save(commit = False)
            profile.user = request.user
            profile.save()

        else:
            return render(request, self.template_name, {'errors': form.errors})

        return redirect('resume:experiences')

# class ExperienceList(generic.DetailView):
# class EducationAdd(generic.DetailView):
# class EducationList(generic.DetailView)::
# class ProjectAdd(generic.DetailView):
# class ProjectList(generic.DetailView):
