from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

urlpatterns = patterns('',

    url(r'^$', views.IndexView.as_view(), name="index"),

    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name="detail"),

    url(r'^delete/(?P<pk>\d+)/$', views.delete, name="delete"),

    url(r'^edit/(?P<pk>\d+)/$', views.EditView.as_view(), name="edit"),

    url(r'^update/(?P<pk>\d+)/$', views.update, name="update"),

    url(r'^new/$', views.new_form, name="new"),

    url(r'^create/$', views.new, name="create"),


)
