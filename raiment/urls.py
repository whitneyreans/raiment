from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^community', views.community, name='community'),
    url(r'^mood', views.mood, name='mood'),
    url(r'^login', views.login, name='login'),

]