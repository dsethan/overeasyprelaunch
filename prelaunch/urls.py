from django.conf.urls import patterns, url
from prelaunch import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),

    )
