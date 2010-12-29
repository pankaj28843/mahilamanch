from django.conf.urls.defaults import *
from django.contrib import admin
from django.shortcuts import render_to_response
from django.views.generic.simple import direct_to_template

import settings

admin.autodiscover()

urlpatterns = patterns('',
                       (r'^admin/', include(admin.site.urls)),
                       (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'main/login.html'}),
                       (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'main/logout.html'}),
                       (r'^about/$', 'direct_to_template', {"template": "main/about.html"}),
                       (r'^', include("report.urls")),
)
if settings.DEBUG:
    # Set
    mediaURL = settings.MEDIA_URL[1:]
    # Extend
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % mediaURL, 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
