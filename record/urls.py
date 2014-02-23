#encoding=utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'record.views.home', name='home'),
    # url(r'^record/', include('record.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^Contact/$',Contact),
    url(r'^$',HomePage)
)
