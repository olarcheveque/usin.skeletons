# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin_tools/', include('admin_tools.urls')),
    (r'^admin/', include(admin.site.urls)),
)
