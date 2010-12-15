from django.conf.urls.defaults import *
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
                       (r'^admin/', include(admin.site.urls)),
                       (r'', include("report.urls")),
)
if settings.DEBUG:
    # Set
    mediaURL = settings.MEDIA_URL[1:]
    # Extend
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % mediaURL, 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
