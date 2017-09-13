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
from .forms import ProfileForm, ExperienceForm, EducationForm, ProjectForm

class IndexView(generic.ListView):
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

class ProfileUpdate(UpdateView):
    model = Details
    template_name = 'resume/profile_update.html'
    fields = ['first_name', 'last_name', 'birth_date', 'gender', 'contact', 'address', 'facebook', 'github', 'linkedin']

class ExperienceAdd(View):
    form_class = ExperienceForm
    template_name = 'resume/experience_add.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            experience = form.save(commit = False)
            experience.user = request.user
            experience.save()

        else:
            return render(request, self.template_name, {'errors': form.errors})

        return redirect('resume:experiences')

class ExperienceList(generic.ListView):
    template_name = 'resume/experiences.html'
    context_object_name = 'all_experiences'

    def get_queryset(self):
        return Experience.objects.filter(user=request.user)

class ExperienceUpdate(UpdateView):
    model = Experience
    template_name = 'resume/experience_update.html'
    fields = ['company', 'start_date', 'end_date', 'description']

class EducationAdd(View):
    form_class = EducationForm
    template_name = 'resume/education_add.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            education = form.save(commit = False)
            education.user = request.user
            education.save()

        else:
            return render(request, self.template_name, {'errors': form.errors})

        return redirect('resume:educations')

class EducationList(generic.ListView):
    template_name = 'resume/educations.html'
    context_object_name = 'all_education'

    def get_queryset(self):
        return Education.objects.filter(user=request.user)

class EducationUpdate(UpdateView):
    model = Experience
    template_name = 'resume/experience_update.html'
    fields = ['institution_name', 'degree', 'start_year', 'end_year']

class ProjectAdd(View):
    form_class = ProjectForm
    template_name = 'resume/project_add.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            project = form.save(commit = False)
            project.user = request.user
            project.save()

        else:
            return render(request, self.template_name, {'errors': form.errors})

        return redirect('resume:projects')

class ProjectList(generic.ListView):
    template_name = 'resume/projects.html'
    context_object_name = 'all_projects'

    def get_queryset(self):
        return Project.objects.filter(user=request.user)

class ProjectUpdate(UpdateView):
    model = Project
    template_name = 'resume/project_update.html'
    fields = ['title', 'description', 'url', 'image_file']
