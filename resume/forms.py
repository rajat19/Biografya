from .models import Details
from django import form, template

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Details
        fields = ['first_name', 'last_name', 'birth_date', 'gender', 'contact', 'address', 'facebook', 'github', 'linkedin', 'photo']

class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = ['company', 'start_date', 'end_date', 'description']
