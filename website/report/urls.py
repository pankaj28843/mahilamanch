from django.conf.urls.defaults import *


urlpatterns = patterns('report.views',
    url(r'^$', 'index', name='index'),
    url(r'^add/district/$', 'add_district', name='add_district'),
    url(r'^add/block/$', 'add_block', name='add_block'),
    url(r'^add/health-center/$', 'add_health_center', name='add_health_center'),
    url(r'^add/event/$', 'add_event', name='add_event'),
    #url(r'^edit/district/$', 'district_list_edit', name='district_list_edit'),
    #url(r'^edit/block/$', 'block_list_edit', name='block_list_edit'),
    #url(r'^edit/health-center/$', 'health_center_list_edit', name='health_center_list_edit'),
    url(r'^feeds/block-by-district-name/(?P<district_name>.*)/$', 'feeds_block_list', name='feeds_block_list'),
    url(r'^feeds/district-center/(?P<district_name>.*)/$', 'feeds_district_center', name='feeds_district_center'),
    url(r'^feeds/block-center/(?P<block_name>.*)/$', 'feeds_block_center', name='feeds_block_center'),
    url(r'^feeds/health-center-position/(?P<block_name>.*)/$', 'feeds_block_center', name='feeds_block_center'),
)