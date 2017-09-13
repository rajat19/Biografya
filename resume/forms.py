from .models import Details, Experience, Education, Project
from django import forms, template

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Details
        fields = ['first_name', 'last_name', 'birth_date', 'gender', 'contact', 'address', 'facebook', 'github', 'linkedin', 'photo']

class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = ['company', 'start_date', 'end_date', 'description']

class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ['institution_name', 'degree', 'start_year', 'end_year']

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['title', 'description', 'url', 'image_file']
