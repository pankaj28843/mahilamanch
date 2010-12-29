from django.conf.urls.defaults import *


urlpatterns = patterns('report.views',
    url(r'^$', 'index', name='index'),
    url(r'^report/$', 'excelview', name='excelview'),
    url(r'^add/district/$', 'add_district', name='add_district'),
    url(r'^add/block/$', 'add_block', name='add_block'),
    url(r'^add/health-center/$', 'add_health_center', name='add_health_center'),
    url(r'^add/event/$', 'add_event', name='add_event'),
    url(r'^edit/district/$', 'district_list_edit', name='district_list_edit'),
    url(r'^edit/district/(?P<district_name>.*)/$', 'edit_district', name='edit_district'),
    url(r'^delete/district/(?P<district_name>.*)/$', 'delete_district', name='delete_district'),

    url(r'^edit/block/$', 'block_list_edit', name='block_list_edit'),
    url(r'^edit/block/(?P<block_name>.*)/$', 'edit_block', name='edit_block'),
    url(r'^delete/block/(?P<block_name>.*)/$', 'delete_block', name='delete_block'),

    url(r'^edit/health-center/$', 'health_center_list_edit', name='health_center_list_edit'),
    url(r'^edit/health-center/(?P<health_center_name>.*)/$', 'edit_health_center', name='edit_health_center'),
    url(r'^delete/health-center/(?P<health_center_name>.*)/$', 'delete_health_center', name='delete_health_center'),
    url(r'^feeds/block-by-district-name/(?P<district_name>.*)/$', 'feeds_block_list', name='feeds_block_list'),
    url(r'^feeds/district-center/(?P<district_name>.*)/$', 'feeds_district_center', name='feeds_district_center'),
    url(r'^feeds/block-center/(?P<block_name>.*)/$', 'feeds_block_center', name='feeds_block_center'),
    url(r'^feeds/health-center-position/(?P<block_name>.*)/$', 'feeds_block_center', name='feeds_block_center'),
)
