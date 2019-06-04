from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.intro, name='intro'),
    url(r'^index/$', views.index, name='index'),
    url(r'^profile/update/$', views.update_profile, name='update_profile'),
    url(r'^profile/$', views.profile, name='profile'),
]