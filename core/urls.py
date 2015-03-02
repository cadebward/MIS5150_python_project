from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

urlpatterns = patterns('',

    url(r'^$', views.IndexView.as_view(), name="index"),

    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name="detail"),

    url(r'^new/$', views.new_form, name="new"),

    url(r'^create/$', views.new, name="create"),

)
