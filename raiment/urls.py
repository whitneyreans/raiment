from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^community', views.community, name='community'),
    url(r'^mood', views.mood, name='mood'),
    url(r'^login$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^create_user$', views.create_user, name='create_user'),


]