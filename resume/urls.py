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

    # /resume/experience/3/update/
    url(r'^experience/(?P<pk>[0-9]+)/update/$', views.ExperienceUpdate.as_view(), name='experience-update'),

    # /resume/education/add
    url(r'^education/add/$', views.ExperienceAdd.as_view(), name='education-add'),

    # /resume/educations/
    url(r'^educations/$', views.EducationList.as_view(), name='educations'),

    # /resume/education/3/update/
    url(r'^education/(?P<pk>[0-9]+)/update/$', views.EducationUpdate.as_view(), name='education-update'),

    # /resume/project/add
    url(r'^project/add/$', views.ProjectAdd.as_view(), name='project-add'),

    # /resume/projects/
    url(r'^projects/$', views.ProjectList.as_view(), name='projects'),

    # /resume/experience/3/update/
    url(r'^project/(?P<pk>[0-9]+)/update/$', views.ProjectUpdate.as_view(), name='project-update'),
]
