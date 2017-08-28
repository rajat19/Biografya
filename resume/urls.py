from django.conf.urls import url
from . import views

app_name = 'resume'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /resume/profile/create
    url(r'^profile/create/$', views.ProfileCreate.as_view(), name='profile-create'),

    # /resume/profile/update
    url(r'^profile/update/$', views.ProfileUpdate.as_view(), name='profile-update'),

    # /resume/experience/add
    url(r'^experience/add/$', views.ExperienceAdd.as_view(), name='experience-add'),

    # /resume/experiences/
    url(r'^experiences/$', views.ExperienceList.as_view(), name='experiences'),

    # /resume/education/add
    url(r'^education/add/$', views.ExperienceAdd.as_view(), name='education-add'),

    # /resume/educations/
    url(r'^education/$', views.EducationList.as_view(), name='education'),

    # /resume/project/add
    url(r'^project/add/$', views.ProjectAdd.as_view(), name='project-add'),

    # /resume/projects/
    url(r'^projects/$', views.ProjectList.as_view(), name='projects'),
]
