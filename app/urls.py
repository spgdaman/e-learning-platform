from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.intro, name='intro'),
    url(r'^index/$', views.index, name='index'),
    url(r'^profile/update/$', views.update_profile, name='update_profile'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^courses/$', views.courses, name='courses'),
    url(r'^submit/assignment/$', views.submit_assignment, name="submit_assignment"),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^pdf_view/(\d+)', views.pdf_view, name="pdf_view"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)