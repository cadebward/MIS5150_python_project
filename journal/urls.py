from django.conf.urls import patterns, include, url
from django.contrib import admin

from core import views

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^entries/', include('core.urls')),

)
