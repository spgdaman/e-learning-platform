from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.intro, name='intro'),
    url(r'^index/$', views.index, name='index'),
    url(r'^profile/update/$', views.update_profile, name='update_profile'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^enroll/course/$', views.enroll_course, name='enroll_course'),
    url(r'^submit/assignment/$', views.submit_assignment, name="submit_assignment"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)